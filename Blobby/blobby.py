import datetime
import json
from Blobby.timeconv import sec_to_day
from time import sleep

class Blobby:
    def __init__(self, starting_hunger=0, starting_boredom=0, starting_dirtiness=0, starting_sleepiness=0, starting_digested=0, poop=0, last_check=None):
        self.hunger = starting_hunger
        self.boredom = starting_boredom
        self.sleepiness = starting_sleepiness
        self.dirtiness = starting_dirtiness
        self.digested_food = starting_digested
        self.poop = poop
        self.last_check = last_check or datetime.datetime.utcnow()
        self.last_pooped = datetime.datetime.utcnow()



    def decay(self):
        time_now = datetime.datetime.utcnow()
        time_passed = time_now - self.last_check
        time_passed_in_sec = time_passed.total_seconds()
        amount_per_sec = 1
        old_digested_food = self.digested_food
        total_decay = time_passed_in_sec * amount_per_sec

        self.hunger = max(0, min(int(self.hunger + total_decay), 100))
        self.boredom = max(0, min(int(self.boredom + total_decay), 100))
        self.sleepiness = max(0, min(int(self.sleepiness + total_decay), 100))
        self.digested_food = max(0, min(int(self.digested_food - total_decay), 100))
        poop_amount = (old_digested_food - self.digested_food) * 0.1
        self.poop = max(0, min(int(self.poop + poop_amount), 10))

        self.last_check = time_now

        save(self)


    # def poop(self):
    #     poop_per_day = 1
    #     time_now = datetime.datetime.utcnow()
    #     time_passed = time_now - self.last_pooped
    #     amount_of_poop = int(poop_per_day * (sec_to_day(time_passed.total_seconds())))
    #     print("the amount of poop: ", amount_of_poop)
    #     new_dirtiness = self.dirtiness + amount_of_poop
    #     self.dirtiness = max(0, min(int(new_dirtiness), 100))
    #     self.last_pooped = time_now
    #     save(self)
    #     return


    def clean(self, cleaning=1):
        new_poop = self.poop - cleaning
        self.poop = max(0, min(new_poop, 10))
        save(self)


    def feed(self, portion=5):
        self.decay()
        new_hunger = self.hunger - portion
        self.hunger = max(0, min(new_hunger, 10))
        self.digested_food += portion
        save(self)

    def poop_test(self):
        poop = 0

        if self.feed(portion=5):
            sleep(1)
            poop += 1
            dirtiness_amount = 10
            new_dirtiness = self.dirtiness + dirtiness_amount
            self.dirtiness = max(0, min(int(new_dirtiness), 100))

        if self.clean(cleaning=10):
            poop -= 1

        return poop



    def sleep(self, sleep=10):
        self.decay()
        new_sleepiness = self.sleepiness - sleep
        self.sleepiness = max(0, min(new_sleepiness, 100))
        save(self)


    def play(self, play_time=5):
        self.decay()
        new_boredom = self.boredom - play_time
        self.boredom = max(0, min(new_boredom, 100))
        save(self)

    def inspect_hunger(self):
        return int(self.hunger)

    def inspect_boredom(self):
        return int(self.boredom)

    def inspect_dirtiness(self):
        return int(self.dirtiness)

    def inspect_sleepiness(self):
        return int(self.sleepiness)


    def inspect(self):
        self.decay()
        hunger = Blobby.inspect_hunger(self)
        boredom = Blobby.inspect_boredom(self)
        dirtiness = Blobby.inspect_dirtiness(self)
        sleepiness = Blobby.inspect_sleepiness(self)


        if self.hunger > 60:
            hunger_text = f'Blobby is hungry {hunger}'
        elif self.hunger < 40:
            hunger_text = f'Blobby is fed {hunger}'
        else:
            hunger_text = f'Blobby wouldn\'t mind a snack {hunger}'

        if self.boredom > 60:
            boredom_text = f'Blobby is bored {boredom}'
        elif self.boredom < 40:
            boredom_text = f'Blobby is amused {boredom}'
        else:
            boredom_text = f'Blobby wouldn\'t mind a playtime {boredom}'

        if self.dirtiness > 0:
            dirtiness_text = f'Blobby is dirty! Clean it up {dirtiness}'
        else:
            dirtiness_text = f'Blobby is clean {dirtiness}'

        if self.sleepiness > 50:
            sleepiness_text = f'Blobby is sleepy {sleepiness}'
        else:
            sleepiness_text = f'Blobby is active {sleepiness}'


        return hunger_text, boredom_text, dirtiness_text, sleepiness_text



def save(blobby):
    blobby_stats = {'hunger': blobby.hunger,
                    'boredom': blobby.boredom,
                    'dirtiness': blobby.dirtiness,
                    'sleepiness': blobby.sleepiness,
                    'poop': blobby.poop,
                    'digested': blobby.digested_food,
                    'last_check': blobby.last_check.isoformat()
                    }
    with open('blobby.json', 'w') as blobby_file:
        json.dump(blobby_stats, blobby_file)


def load():
    try:
        with open('blobby.json', 'r') as blobby_file:
            blobs = json.load(blobby_file)
    except Exception as e:
        print(e)
        blobs = {}
    print("blobs,", blobs)

    blobby = Blobby(starting_hunger=blobs.get('hunger', 0),
                    starting_boredom=blobs.get('boredom', 0),
                    starting_dirtiness=blobs.get('dirtiness', 0),
                    starting_sleepiness=blobs.get('sleepiness', 0),
                    starting_digested=blobs.get('digested', 0),
                    poop=blobs.get('poop', 0),
                    last_check=datetime.datetime.fromisoformat(blobs.get('last_check', datetime.datetime.utcnow().isoformat()))
                    )
    return blobby



if __name__ == '__main__':
    try:
        blobby1 = load()
    except Exception:
        blobby1 = Blobby(starting_hunger=0)
    try:
        save(blobby1)
    except SystemExit:
        save(blobby1)
        raise




