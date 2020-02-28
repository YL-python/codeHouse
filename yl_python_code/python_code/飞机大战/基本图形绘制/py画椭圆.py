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

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            
    screen.fill(WHITE)
    pygame.draw.ellipse(screen,BLACK,(100, 100, 400, 200), 1)
    pygame.draw.ellipse(screen,BLACK,(220, 50, 200, 200), 1)
    #画一个（限定）矩形 矩形中画椭圆
    pygame.display.flip()

    clock.tick(10)
