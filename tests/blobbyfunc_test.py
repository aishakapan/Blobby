import pytest
import random
from PIL import Image
from Blobby import blobby, timeconv, bgraphics



def add_poop(current_blobby):
    '''Adds poop to the blobby image at a horizontally random location'''

    poop = Image.open('/home/morkovka/PycharmProjects/Blobby/static/sized_poop.png')
    blobby = Image.open(current_blobby)
    # img_path = 'static/poopy.png'

    alpha_image = Image.alpha_composite(poop, blobby)

    return alpha_image.show()

add_poop('/home/morkovka/PycharmProjects/Blobby/tests/very_happy_test.png')
