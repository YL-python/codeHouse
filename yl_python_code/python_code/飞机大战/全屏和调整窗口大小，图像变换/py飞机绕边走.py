import pygame
import sys  
from pygame.locals import *
pygame.init()

size = width, height = 600, 400
bg = (255, 255, 255) 
speed = [5, 0]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("小宝宝，来玩啊!")

tupian = pygame.image.load("me1.png")
tupian = pygame.transform.rotate(tupian, 180)
position = tupian.get_rect()

tupian_right = pygame.transform.rotate(tupian, 270)
tupian_top = tupian
tupian_left = pygame.transform.rotate(tupian, 90)
tupian_bottom = pygame.transform.rotate(tupian, 180)

while True: 
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            sys.exit()      
  
    position = position.move(speed)

    if position.right > width:
        tupian = tupian_right
        position = tupian_rect = tupian.get_rect()
        position.left = width - tupian_rect.width
        speed = [0, 5]
    if position.bottom > height:
        tupian = tupian_bottom
        position = tupian_rect = tupian.get_rect()
        position.left = width - tupian_rect.width
        position.top = height - tupian_rect.height
        speed = [-5, 0]
    if position.left < 0:
        tupian = tupian_left
        position = tupian_rect = tupian.get_rect()
        position.right = tupian_rect.width
        position.top = height - tupian_rect.height
        speed = [0, -5]
    if position.top < 0:
        tupian = tupian_top
        position = tupian_rect = tupian.get_rect()
        position.bottom = tupian_rect.height
        position.right = tupian_rect.width
        speed = [5, 0]
        

    screen.fill(bg)
    screen.blit(tupian, position)
    pygame.display.flip()
    pygame.time.delay(10)
