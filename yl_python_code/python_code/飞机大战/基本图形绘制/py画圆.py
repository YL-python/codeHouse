import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

size = width,heighe = 600,400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("123456")

position = size[0] // 2, size[1] // 2
moving = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:#表示鼠标点击
            if event.button == 1:#表示鼠标左键
                moving = True
        if event.type == MOUSEBUTTONUP:#表示鼠标松开
            if event.button == 1:#表示鼠标左键
                moving = False
    if moving:
        position = pygame.mouse.get_pos()#获得鼠标位置
                        
    screen.fill(WHITE)
    
    pygame.draw.circle(screen, BLUE, position, 25, 1)
    #在哪画 颜色 位置 半径 线条宽度
    pygame.draw.circle(screen, RED, position, 50, 1)
    pygame.draw.circle(screen, GREEN, position, 75, 1)

    pygame.display.flip()

    clock.tick(10)
