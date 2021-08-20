import datetime
import pickle


def interact(blobby):
    action = input('This is Blobby. You can feed and play with him or inspect his condition. Press F or P or I ')
    if action == 'F':
        blobby.feed()
        blobby.inspect()
    elif action == 'P':
        blobby.play()
        blobby.inspect()
    elif action == 'I':
        blobby.inspect()
    else:
        print('Please enter a valid input. ')


class Blobby:
    def __init__(self, starting_hunger=0, starting_boredom=0):
        self.hunger = starting_hunger
        self.boredom = starting_boredom
        self.last_check = datetime.datetime.utcnow()

    # decreasing over time

    def decay(self):
        time_now = datetime.datetime.utcnow()
        time_passed = time_now - self.last_check
        time_passed_in_sec = time_passed.total_seconds()
        amount_per_sec = 0.001
        total_decay = time_passed_in_sec * amount_per_sec
        self.hunger += total_decay
        self.boredom += total_decay
        self.last_check = time_now



    # if hunger and boredom at 0, no need to feed or play

    def feed(self, portion=10):
        self.decay()
        self.hunger = self.hunger - portion

    # decreasing hunger and boredom by 10

    def inspect(self):
        self.decay()
        if self.hunger > 50:
            hunger = 'Blobby is hungry {}'.format(self.hunger)
        elif self.hunger < 10:
            hunger = 'Blobby is fed {hunger}'.format(hunger = self.hunger)
        else:
            hunger = 'Blobby is {msg} {hunger}'.format(msg = 'peckish', hunger = self.hunger)

        if self.boredom > 50:
            boredom = 'Blobby is bored {}'.format(self.boredom)
        elif self.boredom < 10:
            boredom = 'Blobby is amused {}'.format(self.boredom)
        else:
            boredom = 'Blobby wouldn\'t mind a playtime {}'.format(self.boredom)

        return hunger, boredom


    def play(self, play_time=10):
        self.decay()
        self.boredom = self.boredom - play_time

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
        blobby1 = Blobby(starting_hunger=50)
    try:
        while True:
            interact(blobby = blobby1)
            save(blobby1)
    except KeyboardInterrupt:
        save(blobby=blobby1)
    except SystemExit:
        save(blobby1)
        raise




