from src.locals import *
from src.game import *

import random


def create_food(snake):
    food_x = random.randint(0, gm_c - 1)
    food_y = random.randint(0, gm_r - 1)

    while Point(food_x, food_y) in snake:
        food_x = random.randint(0, gm_c - 1)
        food_y = random.randint(0, gm_r - 1)

    return Point(food_x, food_y)
