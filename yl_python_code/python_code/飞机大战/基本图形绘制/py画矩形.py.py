import pygame
import sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = width,heighe = 600,400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("123456")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                        
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLACK, (50,50,150,50), 0)
    pygame.draw.rect(screen, BLACK, (250,100,150,50), 1)

    #rect（画矩形）的四个参数 在哪绘制图形 什么颜色
    #(x,y,m,n)左端靠右x像素 上端靠下y像素 矩形宽m 高n
    #最后一个数值  0表示填充颜色 1表示不填充 >1表示画矩形线宽（宽度是数值的一半）
    
    pygame.display.flip()

    clock.tick(10)
