import pygame
import sys
from pygame.locals import *
import math

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

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            
    screen.fill(WHITE)
    pygame.draw.arc(screen, BLACK, (100,100,440,100),0,math.pi,1)
    pygame.draw.arc(screen, BLACK, (220,50,200,200),math.pi,math.pi*2,1)
    #取椭圆的弧线   开始弧度到结束弧度
    pygame.display.flip()

    clock.tick(10)
