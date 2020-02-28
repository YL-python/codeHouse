import pygame
import sys
from pygame.locals import *
from random import *

#pygame内置的sprite函数

# spritecollide(sprite, group, dokill, collided = Npne)
# 精灵 精灵组 检测完后是否删除精灵组中与精灵碰撞的精灵 定制特殊的检测方法
# 精灵组是需要sprite 特定的组
# 因为图片是矩形而需要检测的是圆形所以需要传入第四个参数

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
    group = pygame.sprite.Group()
    # 创建sprite 特定的组
    
    #生成五个随机位置 随机速度的球
    for i in range(5):
        #62是球图片的尺寸
        position = (randint(0, width - 62), randint(0, height - 62))
        speed = [randint(-5, 5), randint(-5, 5)]
        ball = Ball(ball_image, position, speed, bg_size)
        while pygame.sprite.spritecollide(ball, group, False):
            ball.rect.left, ball.rect.top = randint(0, width - 62), randint(0, height - 62)

        balls.append(ball)
        group.add(ball)

    clock = pygame.time.Clock()#设置帧率
                              
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background, (0, 0))

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)

        for each in group:
            group.remove(each)
            
            if pygame.sprite.spritecollide(each, group, False):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]

            group.add(each)
            
        pygame.display.flip()
        clock.tick(30)
        
if __name__ == "__main__":
    main()
