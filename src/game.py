from src.locals import *


def pot_2_pos(pot):
    return gm_x1 + pot.x * gd_size, gm_y1 + pot.y * gd_size


def out_of_gm(p):
    return not (0 <= p.x < gm_c and 0 <= p.y < gm_r)
