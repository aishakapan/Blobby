import datetime
import pickle



class Blobby:
    def __init__(self, starting_hunger=0, starting_boredom=0):
        self.hunger = starting_hunger
        self.boredom = starting_boredom
        self.last_check = datetime.datetime.utcnow()



    def decay(self):
        time_now = datetime.datetime.utcnow()
        time_passed = time_now - self.last_check
        time_passed_in_sec = time_passed.total_seconds()
        amount_per_sec = 0.1
        total_decay = time_passed_in_sec * amount_per_sec
        self.hunger += total_decay
        self.boredom += total_decay
        self.last_check = time_now


    def feed(self, portion=5):
        self.decay()
        new_hunger = self.hunger - portion
        self.hunger = max(0, min(new_hunger, 50))


    def play(self, play_time=5):
        self.decay()
        new_boredom = self.boredom - play_time
        self.boredom = max(0, min(new_boredom, 50))

    def inspect_hunger(self):
        return int(self.hunger)

    def inspect_boredom(self):
        return int(self.boredom)

    def inspect(self):
        self.decay()
        hunger = Blobby.inspect_hunger(self)
        boredom = Blobby.inspect_boredom(self)

        if self.hunger > 40:
            hunger = 'Blobby is hungry {}'.format(hunger)
        elif self.hunger < 10:
            hunger = 'Blobby is fed {}'.format(hunger)
        else:
            hunger = 'Blobby is  hungry {}'.format(hunger)

        if self.boredom > 40:
            boredom = 'Blobby is bored {}'.format(boredom)
        elif self.boredom < 10:
            boredom = 'Blobby is amused {}'.format(boredom)
        else:
            boredom = 'Blobby wouldn\'t mind a playtime {}'.format(boredom)

        return hunger, boredom




def save(blobby):
    with open('blobby.pkl', 'wb') as blobby_file:
        pickle.dump(blobby, blobby_file)

def load():
    with open('blobby.pkl', 'rb') as blobby_loading:
        blobs = pickle.load(blobby_loading)
    return blobs



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




