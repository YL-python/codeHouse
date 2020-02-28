#写入我方飞机所有信息
import pygame

class Myplane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)#初始化Sprite函数

        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
        self.destroy_images = []#装飞机爆炸的图片
        self.destroy_images.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_2.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_3.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_4.png").convert_alpha()\
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        
        #起始位置
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 10
        self.active = True   #标记飞机飞行状态  True时飞机正常飞行 碰撞了就变False然后播放爆炸图片
        self.invincible = False#无敌
        self.mask = pygame.mask.from_surface(self.image1)#用于碰撞检测 mask装图片非透明部分

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0


    def moveDown(self):
        if self.rect.bottom < self.height:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height    

    def moveLeft(self):
        if self.rect.left > -48:
            self.rect.left -= self.speed
        else:
            self.rect.left = -48

    def moveRight(self):
        if self.rect.right < self.width + 46:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width + 46

    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True
