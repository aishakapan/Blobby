import datetime
import pickle
from PIL import Image
import random



class Blobby:
    def __init__(self, starting_hunger=0, starting_boredom=0, starting_dirtiness=0, starting_sleepiness=0):
        self.hunger = starting_hunger
        self.boredom = starting_boredom
        self.sleepiness = starting_sleepiness
        self.dirtiness = starting_dirtiness
        self.last_check = datetime.datetime.utcnow()
        self.last_pooped = datetime.datetime.utcnow()



    def decay(self):
        time_now = datetime.datetime.utcnow()
        time_passed = time_now - self.last_check
        time_passed_in_sec = time_passed.total_seconds()
        amount_per_sec = 0.001
        total_decay = time_passed_in_sec * amount_per_sec
        self.hunger = max(0, min(int(self.hunger + total_decay), 100))
        self.boredom = max(0, min(int(self.boredom + total_decay), 100))
        self.sleepiness = max(0, min(int(self.sleepiness + total_decay), 100))
        self.last_check = time_now


    def poop(self):
        poop_per_day = 10
        time_now = datetime.datetime.utcnow()
        time_passed = time_now - self.last_pooped
        amount_of_poop = poop_per_day * time_passed.total_seconds()
        new_dirtiness = self.dirtiness + amount_of_poop
        self.dirtiness = max(0, min(int(new_dirtiness), 100))
        self.last_pooped = time_now

        return


    def clean(self, cleaning=10):
        new_dirtiness = self.dirtiness - cleaning
        self.dirtiness = max(0, min(new_dirtiness, 100))


    def feed(self, portion=5):
        self.decay()
        new_hunger = self.hunger - portion
        self.hunger = max(0, min(new_hunger, 10))

    def sleep(self, sleep=10):
        self.decay()
        new_sleepiness = self.sleepiness - sleep
        self.sleepiness = max(0, min(new_sleepiness, 100))


    def play(self, play_time=5):
        self.decay()
        new_boredom = self.boredom - play_time
        self.boredom = max(0, min(new_boredom, 100))

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
    with open('blobby.pkl', 'wb') as blobby_file:
        pickle.dump(blobby, blobby_file)


def load():
    with open('blobby.pkl', 'rb') as blobby_loading:
        blobs = pickle.load(blobby_loading)
    return blobs


def add_poop(num, current_blobby):
    '''Adds poop to the blobby image at a horizontally random location'''

    poop = Image.open('/home/morkovka/PycharmProjects/Blobby/static/sized_poop.png')
    img_path = 'static/poopy.png'

    original_image = Image.open(current_blobby)
    image = original_image.copy()
    for i in range(num):
        rand_pos = random.randint(-250, 251)
        image.paste(poop, (rand_pos, 50), poop)
    image.save(img_path)

    return img_path


if __name__ == '__main__':
    try:
        blobby1 = load()
    except Exception:
        blobby1 = Blobby(starting_hunger=0)
    try:
        while True:
            save(blobby1)
    except SystemExit:
        save(blobby1)
        raise




