import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

points = [(200,70), (300, 25), (400, 75), (450, 25), (450, 125), (400, 75), (300, 125)]

size = width,heighe = 600,400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("123456")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                        
    screen.fill(WHITE)
    
    pygame.draw.polygon(screen, BLUE, points, 0)

    pygame.display.flip()

    clock.tick(10)
