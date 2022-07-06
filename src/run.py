from src import welcome
from src.login import player_name
import pygame,sys,random
from collections import deque
from pygame.locals import *
from src.font.font import *
from src.locals import *
from src.controls import *
from src.game import *
from src.food import *
import time
from math import ceil
#from src import login 无效
from src.db.crud import get_score,upd_score

pygame.init()
# 创建一个窗体对象screen
global screen
screen = pygame.display.set_mode(wd_size)
# 指定窗体的标题
pygame.display.set_caption("贪吃蛇")

def end_score(score,high_score):
    if score > high_score:
        upd_score(player_name,score)

class Init_snake():
    def init_snake(self):
        xx,yy=(gm_W)/2/25,0
        snake=deque()
        snake.append(Point(xx,yy+2))
        snake.append(Point(xx,yy+1))
        snake.append(Point(xx,yy))
        return snake

class Draw_snake():
    def draw_snake(self,snake):
        for s in snake:
            pos_x,pos_y=pot_2_pos(s)
            pygame.draw.rect(screen,snake_color,(pos_x,pos_y,gd_size,gd_size))

class Draw_food():
    def draw_food(self,food):
        pos_x, pos_y = pot_2_pos(Point(food.x, food.y))
        pos_x += gd_size / 2
        pos_y += gd_size / 2
        pygame.draw.circle(screen,food_color,(pos_x,pos_y),gd_size/2)


isk = Init_snake()
snake = isk.init_snake()
food = create_food(snake)
high_score = get_score(player_name)

lk=True
# 死亡标志，保证初始时不显示gameover，暂停标志
game_over,game_start,pause = True,False,False
orispeed=0.3  #蛇初始速度
pos,speed,score=(0,1),orispeed,0  #蛇速度
last_move_time=time.time()

txt_font1 = pygame.font.Font('src/font/8-bit.ttf', 50)
txt_font2 = pygame.font.Font('src/font/8-bit.ttf', 80)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:#用户点了关闭
            end_score(score,high_score)
            sys.exit()
        elif event.type==KEYDOWN:#print(event)查看键号
            if event.key == K_RETURN:
                if game_over:
                    score, speed, game_over,game_start, lk = 0, orispeed, False, True,True
                    last_move_time = time.time()
                    isk=Init_snake()
                    snake = isk.init_snake()
                    food = create_food(snake)
                    high_score = get_score(player_name)
                    pos=(0,1)
            if event.key==K_SPACE:
                if not game_over:
                    pause=not pause
            else :
                lk,pos =  cvt_drt(event.key,lk,pos)


    if not game_over:
        curTime=time.time()
        if curTime-last_move_time>speed: ###
            if not pause:
                lk=True
                last_move_time=curTime
                next_s = Point(snake[0].x + pos[0], snake[0].y + pos[1])

                if next_s == food:
                    snake.appendleft(next_s)
                    score+=10;
                    speed = max(0.06,orispeed-0.03*(score//30))
                    food = create_food(snake)
                else:
                    snake.pop()
                    if out_of_gm(next_s) or next_s in snake:
                        game_over = True
                    else:
                        snake.appendleft(next_s)

    screen.fill(bg_color)
    pygame.draw.rect(screen, line_color, (gm_x1,gm_y1, gm_W, gm_H),2)#可以改为最后画线
    #实例化画蛇类和画食物类
    ds,df=Draw_snake(),Draw_food()
    ds.draw_snake(snake)
    df.draw_food(food)


    fwidth, fheight = txt_font2.size('GAME OVER')

    if game_over:
        if game_start:
            end_score(score,high_score)
            gox,goy=pot_2_pos(Point(gm_c/2,gm_r/2))
            Print_Txt(screen, txt_font2, gox - fwidth / 2, goy - fheight / 2, 'GAME OVER')

    Print_Txt(screen, txt_font1, 125, 73, f'level: {ceil((orispeed - speed) / 0.03 + 1)}')
    Print_Txt(screen, txt_font1, 340, 73, f'score: {score}')
    Print_Txt(screen, txt_font1, 550, 73, f'high score: {high_score}')

    pygame.display.update()


