from src.locals import *
import pygame

def Print_Txt(screen,font,x,y,text,fcolor=font_color):
    #font.render参数意义：.render（内容，是否抗锯齿，字体颜色，字体背景颜色）
    Text=font.render(text,True,fcolor)
    screen.blit(Text,(x,y))