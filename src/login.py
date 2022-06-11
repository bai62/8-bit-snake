#含边界判定，有计数显示，可以暂停
from src.font.font import *
import pygame
from src.locals import *
from src.game import *
import pygame.locals
import pygame.freetype
from src.db.crud import *

size=width,height=566,565#与下面的图片的大小，如果不一致会导致图片显示不完全，或者产生缝隙
black=0,0,0

pygame.init()#初始化init()及设置
screen=pygame.display.set_mode(wd_size)#窗口大小
pygame.display.set_caption("贪吃蛇")#窗口名字

player_name=''
# f1 = pygame.freetype.Font('font/8-bit.ttf', size=50)#调出文字的字体
txt_font1 = pygame.font.Font('src/font/8-bit.ttf', 36)

usrx,usry=pot_2_pos(Point(4,4))
pswx,pswy=pot_2_pos(Point(4,6))
infgw,infgh = gd_size*8,gd_size*1.2 #6/5
rgsgw,rgsgh = gd_size*5.8,gd_size*1.2
lgngw,lgngh = gd_size*3.8,gd_size*1.2
usrgx,usrgy=pot_2_pos(Point(10,4))
pswgx,pswgy=pot_2_pos(Point(10,6))
rgsgx,rgsgy=pot_2_pos(Point(4,14))
lgngx,lgngy=pot_2_pos(Point(15,14))
#密码错误弹窗
errgx,errgy=pot_2_pos(Point(7,5))
errgw,errgh=gd_size*16,gd_size*7
#密码错误弹窗确认键
errbx,errby=pot_2_pos(Point(14,10))
errbw,errbh=2*gd_size,1.2*gd_size

#pygame.draw.rect(screen, WHITESMOKE, (230, 210, 200, 35))
a,b=[],[]#创建两个空列表，用来分别存储用户名和密码
logo = pygame.image.load("src/UI/logo.png").convert_alpha()

def alert(str1,str2,str3):
    pygame.draw.rect(screen, bg_color, (errgx, errgy, errgw, errgh))
    pygame.draw.rect(screen, line_color, (errgx, errgy, errgw, errgh), 2)
    pygame.draw.rect(screen, bg_color, (errbx, errby, errbw, errbh))
    pygame.draw.rect(screen, line_color, (errbx, errby, errbw, errbh), 2)
    Print_Txt(screen,txt_font1,errgx+gd_size,errgy+gd_size,str1)
    Print_Txt(screen,txt_font1,errgx+gd_size,errgy+2.2*gd_size,str2)
    Print_Txt(screen,txt_font1,errbx+8,errby+6,str3)
    pygame.display.update()

def err_wa(str1,str2,str3):
    alert(str1,str2,str3)

    flag=1
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if errbx <= mouse_x <= errbx + errbw and errby <= mouse_y <= errby + errbh:
                    flag=0


def usr_psw_init():
    screen.fill(bg_color)
    pygame.draw.rect(screen, line_color, (gm_x1, gm_y1, gm_W, gm_H), 2)
    Print_Txt(screen, txt_font1, usrx, usry, "username")
    Print_Txt(screen, txt_font1, pswx, pswy, "password")
    pygame.draw.rect(screen, line_color, (usrgx, usrgy, infgw, infgh), 2)
    pygame.draw.rect(screen, line_color, (pswgx, pswgy, infgw, infgh), 2)

    screen.blit(logo, (600, 330))

def login_init():
    usr_psw_init()
    Print_Txt(screen,txt_font1,rgsgx+5,rgsgy+6,"register")
    Print_Txt(screen,txt_font1,lgngx+5,lgngy+6,"login")
    pygame.draw.rect(screen, line_color, (rgsgx, rgsgy, rgsgw, rgsgh), 2)
    pygame.draw.rect(screen, line_color, (lgngx, lgngy, lgngw, lgngh), 2)


def register_init():
    usr_psw_init()
    Print_Txt(screen, txt_font1, lgngx + 5, lgngy + 6, "register")
    pygame.draw.rect(screen, line_color, (lgngx, lgngy, rgsgw, rgsgh), 2)

def register():
    flag,wz=True,True
    a, b = [], []
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()  # 鼠标的点击位置
                if usrgx <= mouse_x <= usrgx + infgw and usrgy <= mouse_y <= usrgy + infgh:  # 判断点击了哪一个输入框
                    wz = True  # 用于改变后文文字输入显示的位置
                elif pswgx <= mouse_x <= pswgx + infgw and pswgy <= mouse_y <= pswgy + infgh:
                    wz = False
                elif lgngx <= mouse_x <= lgngx + rgsgw and lgngy <= mouse_y < lgngy + rgsgh:
                    if str_a == "":
                        err_wa('username is empty.','','ok')
                    elif str_b == "":
                        err_wa("password is empty.",'','ok')
                    elif check_name(str_a):  # 查库
                        err_wa("this's a already", "taken name.", "ok")
                        a, b, wz = [], [], True
                    else:
                        add(str_a,str_b,0)
                        player_name=str_a
                        err_wa("Registration success.","","ok")
                        flag = False
            elif event.type == pygame.KEYDOWN:  # 检测按键是否是数字键，通过打印输出判断按键的码
                if 48 <= event.key <= 57:
                    if wz and len(a) < 11:  # 限制输入的长度，利用WZ来更改输入内容的显示位置
                        a.append(event.key - 48)
                    elif wz == False and len(b) < 11:
                        b.append(event.key - 48)
        register_init()
        str_a = ""  # 将输入内容存储到列表
        for i in a:
            str_a += str(i)  # 转化拼接为字符串
        str_b = ""
        for i in b:
            str_b += str(i)
        # 显示字符串

        word = []
        Print_Txt(screen, txt_font1, usrgx + 5, usrgy + 6, str_a)
        Print_Txt(screen, txt_font1, pswgx + 5, pswgy + 6, "*" * len(str_b))
        pygame.display.update()

log,wz = True,True
while log:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.locals.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()#鼠标的点击位置
            if usrgx <= mouse_x <= usrgx+infgw and usrgy <= mouse_y <= usrgy+infgh:#判断点击了哪一个输入框
                wz=True#用于改变后文文字输入显示的位置
            elif pswgx <= mouse_x <= pswgx+infgw and pswgy <= mouse_y <= pswgy+infgh:
                wz = False
            elif rgsgx <= mouse_x <= rgsgx+rgsgw and rgsgy<=mouse_y<=rgsgy+rgsgh:
                register()
                log=False
            elif lgngx <= mouse_x <= lgngx+lgngw and lgngy <= mouse_y < lgngy+lgngh:
                  #  if crud.check:# 查库
                    if check_info(str_a,str_b):
                        err_wa('login success','','ok')
                        #登录成功
                        log,player_name = False,str_a
                    if str_a == "":
                        err_wa('username is empty.','','ok')
                    elif str_b == "":
                        err_wa("password is empty.",'','ok')
                    else:
                        err_wa("wrong username or","password.","ok")
                        a,b,wz=[],[],True

        elif event.type == pygame.KEYDOWN:#检测按键是否是数字键，通过打印输出判断按键的码
            if 48 <= event.key <=57 :
                if wz and len(a)<11:#限制输入的长度，利用WZ来更改输入内容的显示位置
                    a.append(event.key-48)
                elif wz==False and len(b)<11:
                    b.append(event.key-48)

    #预处理和动态文字放在一起
    login_init()

    str_a=""#将输入内容存储到列表
    for i in a:
        str_a+=str(i)#转化拼接为字符串
    str_b = ""
    for i in b:
        str_b += str(i)
    #显示字符串

    word=[]
    Print_Txt(screen,txt_font1,usrgx+5,usrgy+6,str_a)
    Print_Txt(screen,txt_font1,pswgx+5,pswgy+6,"*"*len(str_b))

    pygame.display.update()