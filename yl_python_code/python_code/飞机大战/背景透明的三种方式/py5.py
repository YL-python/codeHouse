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
position.center = width // 2, height // 2

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    traget.blit(temp, location)
    #把整体背景透明度调整

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.blit(background,(0, 0))
    screen.blit(tupian, position)

    pygame.display.flip()

    clock.tick(30)

