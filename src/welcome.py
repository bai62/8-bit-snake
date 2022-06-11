import pygame
import time
from src.locals import *
from src.font.font import *
pygame.init()
# 创建一个窗体对象screen
global screen
screen = pygame.display.set_mode(wd_size)
# 指定窗体的标题
pygame.display.set_caption("贪吃蛇")


welcome_font1 = pygame.font.Font('src/font/8-bit.ttf', 110)

screen.fill(bg_color)
st_time = time.time()
Print_Txt(screen, welcome_font1, gm_W/2-2*gd_size, gm_H/2+gd_size, "welcome")
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if time.time()-st_time>2:
        break
