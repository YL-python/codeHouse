import pygame
import sys
from pygame import *

pygame.init()

size = width, height = 480, 700
bg =(0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("  ")

tupian = pygame.image.load("me1.jpg").convert()
background = pygame.image.load("background.jpg").convert()
position = tupian.get_rect()
position.center = width // 2, height // 2#修改图片起始位置

#tupian.set_colorkey((0, 0, 0))#指定一个颜色透明
#tupian.set_alpha(200)#设置整个图片透明度 [0, 255]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.blit(background,(0, 0))
    screen.blit(tupian, position)

    pygame.display.flip()

    clock.tick(30)
