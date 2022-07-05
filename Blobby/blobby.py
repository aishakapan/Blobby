import datetime
import pickle
from PIL import Image
import random



class Blobby:
    def __init__(self, starting_hunger=0, starting_boredom=0, starting_dirtiness=0):
        self.hunger = starting_hunger
        self.boredom = starting_boredom
        self.dirtiness = starting_dirtiness
        self.last_check = datetime.datetime.utcnow()
        self.last_pooped = datetime.datetime.utcnow()



    def decay(self):
        time_now = datetime.datetime.utcnow()
        time_passed = time_now - self.last_check
        time_passed_in_sec = time_passed.total_seconds()
        amount_per_sec = 0.001
        total_decay = time_passed_in_sec * amount_per_sec
        self.hunger = max(0, min(int(self.hunger + total_decay), 50))
        self.boredom = max(0, min(int(self.boredom + total_decay), 50))
        self.last_check = time_now


    def poop(self):
        has_pooped = False
        poop_per_day = 10

        time_now = datetime.datetime.utcnow()
        time_passed = time_now - self.last_pooped
        if time_passed >= datetime.timedelta(seconds=1):
            new_dirtiness = self.dirtiness + poop_per_day
            self.dirtiness = max(0, min(new_dirtiness, 100))
            self.last_pooped = time_now
            has_pooped = True
        return has_pooped


    def clean(self, cleaning=10):
        new_dirtiness = self.dirtiness - cleaning
        self.dirtiness = max(0, min(new_dirtiness, 100))


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

    def inspect_dirtiness(self):
        return int(self.dirtiness)


    def inspect(self):
        self.decay()
        hunger = Blobby.inspect_hunger(self)
        boredom = Blobby.inspect_boredom(self)
        dirtiness = Blobby.inspect_dirtiness(self)


        if self.hunger > 40:
            hunger = f'Blobby is hungry {hunger}'
        elif self.hunger < 10:
            hunger = f'Blobby is fed {hunger}'
        else:
            hunger = f'Blobby is  hungry {hunger}'

        if self.boredom > 40:
            boredom = f'Blobby is bored {boredom}'
        elif self.boredom < 10:
            boredom = f'Blobby is amused {boredom}'
        else:
            boredom = f'Blobby wouldn\'t mind a playtime {boredom}'

        if self.dirtiness > 0:
            dirtiness = f'Blobby is dirty! Clean it up {dirtiness}'
        else:
            dirtiness = f'Blobby is clean {dirtiness}'





        return hunger, boredom, dirtiness



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




