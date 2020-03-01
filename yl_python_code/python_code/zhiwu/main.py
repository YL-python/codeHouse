import pygame

import time

import random

import sys

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 560


# 地图类 v1.2 完善地图类

class Map:
    images_list = ['imgs/map1.png', 'imgs/map2.png']

    def __init__(self, x, y, image_index):
        self.position = (x, y)

        self.image = pygame.image.load(Map.images_list[image_index])

        # v1.5 新增是否能种植的属性

        self.can_grow = True

    # 将当前地图的图片加入到窗口

    def display_map(self):
        MainGame.window.blit(self.image, self.position)


# 植物类 (父类)

class Plant(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.live = True


# 向日葵类 v1.4 完善向日葵类

class Sunflower(Plant):

    def __init__(self, x, y):
        super(Sunflower, self).__init__()

        self.image = pygame.image.load('imgs/sunflower.png')

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.price = 50

        self.hp = 100

        # v1.6 时间计数器

        self.time_count = 0

    # v1.6 新增功能：生成阳光

    def produce_money(self):
        self.time_count += 1

        if self.time_count == 25:
            MainGame.money += 5

            self.time_count = 0

    # 向日葵加入到窗口中

    def display_sunflower(self):
        MainGame.window.blit(self.image, self.rect)


# 豌豆射手类

# v1.5 完善 豌豆射手类

class PeaShooter(Plant):

    def __init__(self, x, y):

        super(PeaShooter, self).__init__()

        # self.image 为一个 surface

        self.image = pygame.image.load('imgs/1-4.png')

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.price = 50

        self.hp = 200

        # v1.7 发射计数器

        self.shot_count = 0

    # v1.7 增加射击方法

    def shot(self):

        # v1.9 记录是否应该射击

        should_fire = False

        for zombie in MainGame.zombie_list:

            if zombie.rect.y == self.rect.y and zombie.rect.x < 800 and zombie.rect.x > self.rect.x:
                should_fire = True

        # 如果活着

        if self.live and should_fire:

            self.shot_count += 1

            # 计数器到25发射一次

            if self.shot_count == 25:
                # 基于当前豌豆射手的位置，创建子弹

                peabullet = PeaBullet(self)

                # 将子弹存储到子弹列表中

                MainGame.peabullet_list.append(peabullet)

                self.shot_count = 0

    # 将豌豆射手加入到窗口中的方法

    def display_peashooter(self):

        MainGame.window.blit(self.image, self.rect)


# 豌豆子弹类

# v1.6 新增子弹类的功能

class PeaBullet(pygame.sprite.Sprite):

    def __init__(self, peashooter):

        self.live = True

        self.image = pygame.image.load('imgs/1-6.png')

        self.damage = 50

        self.speed = 10

        self.rect = self.image.get_rect()

        self.rect.x = peashooter.rect.x + 40

        self.rect.y = peashooter.rect.y + 25

    def move_bullet(self):

        # 在屏幕范围内，实现往右移动

        if self.rect.x < SCREEN_WIDTH:

            self.rect.x += self.speed

        else:

            self.live = False

    # v1.9 新增，子弹与僵尸的碰撞

    def hit_zombie(self):

        for zombie in MainGame.zombie_list:

            if pygame.sprite.collide_rect(self, zombie):

                # 打中僵尸之后，修改子弹的状态，

                self.live = False

                # 僵尸掉血

                zombie.hp -= self.damage

                if zombie.hp <= 0:
                    zombie.live = False

    def display_peabullet(self):

        MainGame.window.blit(self.image, self.rect)


# 僵尸类

# v1.8 完善僵尸类

class Zombie(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super(Zombie, self).__init__()

        self.image = pygame.image.load('imgs/zombie.png')

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.hp = 1000

        self.damage = 2

        self.speed = 1

        self.live = True

        self.stop = False

    #  v1.8僵尸的移动

    def move_zombie(self):

        if self.live and not self.stop:

            self.rect.x -= self.speed

            if self.rect.x < -80:
                # 调用游戏结束方法

                MainGame().gameOver()

    #  v1.8将僵尸加载到地图中

    def display_zombie(self):

        MainGame.window.blit(self.image, self.rect)


# 游戏主线类

class MainGame:
    # 游戏窗口

    window = None

    # v1.2 新增存储所有坐标点的列表

    points_list = []

    # v1.2 新增存储所有地图块的列表

    maps_list = []

    # v1.4 存储所有植物的列表

    plants_list = []

    # v1.5 记录当前的金钱数

    money = 50

    # v1.7 存储所有豌豆子弹的列表

    peabullet_list = []

    # v1.8 新增存储所有僵尸的列表

    zombie_list = []

    def __init__(self):

        pass

    # 加载游戏窗口

    def init_window(self):

        # 调用显示模块的初始化

        pygame.display.init()

        # 创建窗口

        MainGame.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Surface

    # 获取一个包含指定文字的surface

    def get_surface_with_content(self, content, size, font_name, color):

        # 字体初始化

        pygame.font.init()

        # 创建字体

        font = pygame.font.SysFont(font_name, size)

        # 使用对应的字体绘制surface

        sf = font.render(content, True, color)

        return sf

    # v1.2 新增初始化地图坐标的方法

    def init_points(self):

        for y in range(1, 7):  # (1,6)

            temp_list = []

            for x in range(10):  # 0,9

                point = (x, y)

                temp_list.append(point)

            print(temp_list)

            MainGame.points_list.append(temp_list)

    # v1.2 完成所有地图块的创建，存储到列表中

    def init_maps(self):

        # 遍历列表的长度  points 为大列表中的小列表

        for points in MainGame.points_list:

            temp_map_list = []

            for p in points:

                x = p[0] * 80

                y = p[1] * 80

                if (p[0] + p[1]) % 2 == 0:

                    map = Map(x, y, 1)

                else:

                    map = Map(x, y, 0)

                temp_map_list.append(map)

            # 将存储所有地图的列表存储到大列表中

            MainGame.maps_list.append(temp_map_list)

    # v1.2 将地图加载到窗口中

    def load_maps(self):

        for map_list in MainGame.maps_list:

            for map in map_list:
                map.display_map()

    # v1.4 加载所有的植物

    # v1.5 加载豌豆射手处理

    # v1.7 增加豌豆射手发射处理

    def load_plants(self):

        for plant in MainGame.plants_list:

            # v1.6 优化加载植物的处理逻辑

            if plant.live:

                if isinstance(plant, Sunflower):

                    plant.display_sunflower()

                    plant.produce_money()

                elif isinstance(plant, PeaShooter):

                    plant.display_peashooter()

                    plant.shot()

            else:

                MainGame.plants_list.remove(plant)

    # v1.7 加载所有子弹的方法

    def load_peabullets(self):

        for b in MainGame.peabullet_list:

            if b.live:

                b.display_peabullet()

                b.move_bullet()

                # v1.9 调用子弹是否打中僵尸的方法

                b.hit_zombie()

            else:

                MainGame.peabullet_list.remove(b)

    # v1.8 新增初始化僵尸的方法

    def init_zombies(self):

        for i in range(1, 7):
            dis = random.randint(1, 5) * 200

            zombie = Zombie(800 + dis, i * 80)

            MainGame.zombie_list.append(zombie)

    # v1.8 将所有僵尸加载到地图中

    def load_zombies(self):

        for zombie in MainGame.zombie_list:

            if zombie.live:

                zombie.display_zombie()

                zombie.move_zombie()

            else:

                MainGame.zombie_list.remove(zombie)

    # v1.3 新增事件处理的方法

    def deal_events(self):

        # 获取所有事件

        eventList = pygame.event.get()

        # 遍历事件列表，判断

        for e in eventList:

            if e.type == pygame.QUIT:

                self.gameOver()

            elif e.type == pygame.MOUSEBUTTONDOWN:

                # print('按下鼠标按键')

                print(e.pos)

                # print(e.button)#左键1  按下滚轮2 上转滚轮为4 下转滚轮为5  右键 3

                x = e.pos[0] // 80

                y = e.pos[1] // 80

                print(x, y)

                map = MainGame.maps_list[y - 1][x]

                print(map.position)

                # v1.5 增加创建时候的地图装填判断以及金钱判断

                if e.button == 1:

                    if map.can_grow and MainGame.money >= 50:
                        sunflower = Sunflower(map.position[0], map.position[1])

                        MainGame.plants_list.append(sunflower)

                        print('当前植物列表长度:{}'.format(len(MainGame.plants_list)))

                        map.can_grow = False

                        MainGame.money -= 50

                elif e.button == 3:

                    if map.can_grow and MainGame.money >= 50:
                        peashooter = PeaShooter(map.position[0], map.position[1])

                        MainGame.plants_list.append(peashooter)

                        print('当前植物列表长度:{}'.format(len(MainGame.plants_list)))

                        map.can_grow = False

                        MainGame.money -= 50

    # 游戏开始入口

    def startGame(self):

        # 调用初始化窗口的方法

        self.init_window()

        # v1.2 调用初始化坐标点

        self.init_points()

        # v1.2 调用初始化地图

        self.init_maps()

        # v1.8 调用初始化僵尸的方法

        self.init_zombies()

        while True:
            # 设置窗口的填充色

            MainGame.window.fill((255, 255, 255))

            # v1.5 修改文字加载的位置

            # 调用绘制表面

            sf = self.get_surface_with_content('剩余金钱{}'.format(MainGame.money), 26, 'kaiti', (255, 0, 0))

            # 将包含文字的表面加入到窗口中

            MainGame.window.blit(sf, (260, 10))

            # v1.2 调用加载地图方法

            self.load_maps()

            # v1.3 调用事件处理的方法

            self.deal_events()

            # v1.4 调用加载植物的方法

            self.load_plants()

            # v1.5 金钱随着时间增加

            # MainGame.money += 0.25

            # v1.7 调用加载所有子弹的方法

            self.load_peabullets()

            # v1.8 调用展示僵尸的方法

            self.load_zombies()

            # 调用窗口刷新功能

            pygame.display.update()

            # time.sleep(0.025)

            # v1.7 pygame自己的休眠

            pygame.time.wait(10)

    # 程序结束方法

    def gameOver(self):

        print('僵尸进入了你家后院')

        # 结束程序

        sys.exit()


if __name__ == '__main__':
    game = MainGame()

    game.startGame()