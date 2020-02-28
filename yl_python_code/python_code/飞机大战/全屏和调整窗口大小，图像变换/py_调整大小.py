#调整窗口大小
import pygame
import sys
from pygame.locals import *
pygame.init()

size = width, height = 600, 400
speed = [0,0]
ans = [0,0]
fullscreen = False
bg = (255, 255, 255)

screen = pygame.display.set_mode(size,RESIZABLE)#RESIZABLE参数表示可以修改窗口大小
pygame.display.set_caption("wasd 和 上下左右 控制方向 空格暂停")

tupianname = pygame.image.load("me1.png")
position = tupianname.get_rect()

L_head = tupianname
R_head = pygame.transform.flip(tupianname,True,False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                tupianname = L_head
                speed = [-1,0]
                ans = speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                tupianname = R_head
                speed = [1,0]
                ans = speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                speed = [0,-1]
                ans = speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                speed = [0,1]
                ans = speed
            if event.key == pygame.K_SPACE:
                if ans == speed:
                    speed=[0,0]
                else:
                    speed = ans
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen :
                    size = width, height = 1280, 1024
                    screen = pygame.display.set_mode(size, FULLSCREEN | HWSURFACE)
                else:
                    size = width, height = 600, 400
                    screen = pygame.display.set_mode(size,RESIZABLE)

        #调整窗口大小            
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            width,height = size
            #print(size)
            screen = pygame.display.set_mode(size,RESIZABLE)
            
                
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        tupianname = pygame.transform.flip(tupianname,True,False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(tupianname, position)
    pygame.display.flip()
    pygame.time.delay(9)
'''
import pygame
pygame.init()
pygame.display.list_modes()
查看系统分辨率
'''
