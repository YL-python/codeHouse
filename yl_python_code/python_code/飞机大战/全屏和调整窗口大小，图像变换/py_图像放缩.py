#—缩小 +放大 空格还原
import pygame
import sys  
from pygame.locals import *

pygame.init()

size = width, height = 600, 400
speed = [-2,1]
bg = (255, 255, 255) 

screen = pygame.display.set_mode(size)
pygame.display.set_caption("小宝宝，来玩啊!")

#设置放大缩小比率
ratio  = 1.0

otupian = pygame.image.load("me1.png")
tupian = otupian   #缩放最好不要再原图上面改动

otupian_rect = tupianname.get_rect()
position = tupian_rect = otupian_rect

while True: 
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()      
        if event.type == KEYDOWN:
            if event.key == K_EQUALS and ratio < 2:
                ratio += 0.1;
            if event.key == K_MINUS and ratio > 0.5:
                ratio -= 0.1;
            if event.key == K_SPACE:
                ratio += 0.1;
           tupian = pygame.transform.smoothscale(otupian,(int(otupian_rect.width * ratio),int(otupian_rect.height * ratio)))

            
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        tupianname = pygame.transform.flip(tupianname,True,False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(tupian, position)
    pygame.display.flip()
    pygame.time.delay(10)
