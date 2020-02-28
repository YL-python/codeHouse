import pygame
import sys
from pygame.locals import *
from random import *

#  pygame.sprite.Sprite 动画精灵的基类
class Ball(pygame.sprite.Sprite):
    # 球的图片 球的位置 球的速度
    def __init__(self, image, position, speed, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]

    def move(self):
        #调用move 函数
        self.rect = self.rect.move(self.speed)
        
        if self.rect.right < 0:
            self.rect.left = self.width
        elif self.rect.left > self.width:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = self.height
        elif self.rect.top > self.height:
            self.rect.bottom = 0 
        
def main():
    pygame.init()
    ball_image = "jingling.png"
    bg_image = "screen.png"
    
    running = True

    bg_size = width, height = 600, 400#要与载入背景大小尺寸相同
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("来玩啊，小老弟！")

    background = pygame.image.load(bg_image).convert_alpha()

    #装五个球的信息
    balls = []
    #生成五个随机位置 随机速度的球
    for i in range(5):
        #62是球图片的尺寸
        position = (randint(0, width - 62), randint(0, height - 62))
        speed = [randint(-5, 5), randint(-5, 5)]
        ball = Ball(ball_image, position, speed, bg_size)
        balls.append(ball)

    clock = pygame.time.Clock()#设置帧率
                              
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0, 0))

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
        
        pygame.display.flip()
        clock.tick(30)
        
if __name__ == "__main__":
    main()
