import random
from PIL import Image


def resize_img():
    pass

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