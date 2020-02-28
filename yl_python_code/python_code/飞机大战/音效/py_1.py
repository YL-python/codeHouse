import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("bg_music.ogg")#导入
pygame.mixer.music.set_volume(1)#音量调节
pygame.mixer.music.play()#播方

one_sound = pygame.mixer.Sound("击杀音效.ogg")#导入音效
one_sound.set_volume(0.2)#音量
two_sound = pygame.mixer.Sound("11216.ogg")
two_sound.set_volume(0.2)

#创建小窗口
bg_size = width, height = 300, 200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("测试音乐")

pause_image = pygame.image.load("播放.png").convert_alpha()
unpause_image = pygame.image.load("暂停.png").convert_alpha()
pause_rect = pause_image.get_rect()
pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2,  (height - pause_rect.height) // 2

pause = False  # 一个常量 摁空格暂停在摁继续


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                one_sound.play()
            if event.button == 3:
                two_sound.play()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause

    screen.fill((200, 200, 200))
    
    if pause:
        screen.blit(pause_image, pause_rect)
        pygame.mixer.music.pause()
    else :
        screen.blit(unpause_image, pause_rect)
        pygame.mixer.music.unpause()

    pygame.display.flip()
    clock.tick(30)
