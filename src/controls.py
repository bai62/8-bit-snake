from pygame.locals import *

def cvt_drt(key,lk,pos):
    if key in (K_UP, K_w):
        if lk and not pos[1]:  ###
            lk, pos = False, (0, -1)
    elif key in (K_DOWN, K_s):
        if lk and not pos[1]:
            lk, pos = False, (0, 1)
    elif key in (K_LEFT, K_a):
        if lk and not pos[0]:
            lk, pos = False, (-1, 0)
    elif key in (K_RIGHT, K_d):
        if lk and not pos[0]:
            lk, pos = False, (1, 0)
    return lk,pos