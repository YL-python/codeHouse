import pygame
import sys
import traceback
import myplane #导入我们自己写的myplane模块
import enemy
import bullet
import supply
from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

bg_size = width, height =480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("——————飞机大战——————")

background = pygame.image.load("images/background.png").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

def add_small_enemies(group1, group2,num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
        
def add_mid_enemies(group1, group2,num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)
        
def add_big_enemies(group1, group2,num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def inc_speed(target, inc):
    for i in target:
        i.speed += inc

def main():
    pygame.mixer.music.play(-1)

    #生成飞机 调用模块内的函数生成实例化对象 
    me = myplane.Myplane(bg_size)
 
    #用敌机组装所有敌机 碰撞检测
    enemies = pygame.sprite.Group()
    
    small_enemies = pygame.sprite.Group()
    mid_enemies = pygame.sprite.Group()
    big_enemies = pygame.sprite.Group()
    
    #写生成函数 生成小,中,大型飞机并加入两个飞机组中
    add_small_enemies(small_enemies, enemies, 10)
    add_mid_enemies(mid_enemies, enemies, 5)
    add_big_enemies(big_enemies, enemies,1)
    
    #生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

    #生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 8
    for i in range(BULLET2_NUM // 2):
        bullet2.append(bullet.Bullet2((me.rect.centerx - 33, me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx + 30, me.rect.centery)))

    #用来切换我方飞机的图片
    switch_image = True
    
    #用于延迟
    delay = 60

    #记录得分  字体 大小
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 25)

    #表示是否暂停游戏
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()

    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()

    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image  #不在原图上面操作

    #难度级别
    level = 1

    #全屏炸弹
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 3

    #每30秒来一个补给包
    bullet_supply = supply.Bullet_supply(bg_size)
    bomb_supply = supply.Bomb_supply(bg_size)
    SUPPLY_TIME = USEREVENT#自定义事件
    pygame.time.set_timer(SUPPLY_TIME, 30*1000)#30秒触发一次

    #超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1

    #表示是否使用超级子弹
    is_double_bullet = False

    #生命计数器
    LIFE_NUM = 3
    life_image = pygame.image.load("images/life.png").convert_alpha()
    life_rect = life_image.get_rect()

    #无敌计时器
    INVINCIBLE_TIME = USEREVENT + 2

    #阻止一直打开记录分数文件
    recorded = False

   # 游戏结束画面
    gameover_font = pygame.font.Font("font/font.ttf", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()
    
    #飞机爆炸图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    clock = pygame.time.Clock()
    running = True

    while running :
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:#鼠标点击
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME, 0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME, 30*1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
                        
            elif event.type == MOUSEMOTION:#鼠标移动到的位置
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image
                        
            elif event.type == KEYDOWN:#空格引爆炸弹
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for i in enemies:
                            if i.rect.bottom > 0:
                                i.active = False

            elif event.type == SUPPLY_TIME:#响应用户自定义事件
                supply_sound.play()
                if choice([True,False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()

            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME, 0)
            elif event.type == INVINCIBLE_TIME:
                me.invincible = False 
                pygame.time.set_timer(INVINCIBLE_TIME, 0)
                        
        screen.blit(background, (0, 0))

        #根据得分增加难度
        if level == 1 and score > 50000:
            level = 2
            upgrade_sound.play()
            #增加飞机数量来增加难度
            add_small_enemies(small_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 1)
            #增加速度来增加难度
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 200000:
            level = 3
            upgrade_sound.play()
            #增加飞机数量来增加难度
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 1)
            #增加速度来增加难度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 600000:
            level = 4
            upgrade_sound.play()
            #增加飞机数量来增加难度
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #增加速度来增加难度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 1000000:
            level = 5
            upgrade_sound.play()
            #增加飞机数量来增加难度
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            #增加速度来增加难度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        
        if LIFE_NUM and not paused :    
            #检测按键使用时  经常使用最好用Key模块  不经常使用的用事件
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            #绘制炸弹补给
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply,me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            #绘制子弹补给
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply,me):
                    is_double_bullet = True
                    get_bullet_sound.play()
                    pygame.time.set_timer(DOUBLE_BULLET_TIME, 18*1000)
                    bullet_supply.active = False
            

            #画子弹
            if not(delay % 10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33,me.rect.centery))
                    bullets[bullet2_index + 1].reset((me.rect.centerx+30,me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM

                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM

            #检测子弹是否打中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True
                                e.energy = e.energy - 1 
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False

            #绘制大型敌机  这样小敌机就在大敌机上面
            for each in big_enemies:
                if each.active:#存活
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                        
                    #绘制血条  在哪 颜色 始末位置 能量值 宽度
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), 2)
                    #当生命值大于20%显示绿色 否则红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2 :
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), 2)

                    #大敌机有出场音效
                    if each.rect.bottom == -50 :
                        enemy3_fly_sound.play(-1)#-1是循环播放
                else:#毁灭
                    if not(delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect) 
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            score += 10000
                            enemy3_fly_sound.stop()
                            each.reset()

            #画中小敌机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image, each.rect)
                    
                    #绘制血条  在哪 颜色 始末位置 能量值 宽度
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), 2)
                    #当生命值大于20%显示绿色 否则红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2 :
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, each.rect.top - 5), 2)

                else:
                    if not(delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect) 
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 6000
                            each.reset()

            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:  
                    if not(delay % 3):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect) 
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()


            #碰撞检测啦啦啦啦啦啦
            # pygame.sprite.collide_mask 特殊碰撞检测方法 用来检测非透明部分              
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False
            

            #画我方飞机
            if me.active:                
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                if not(delay % 3):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    screen.blit(me.destroy_images[me_destroy_index], me.rect) 
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        LIFE_NUM -= 1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME, 3*1000)

            #画炸弹数量(缩进决定暂停能否看到炸弹数量)
            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))                

            #绘制生命数量
            if LIFE_NUM:
                for i in range(LIFE_NUM):
                    screen.blit(life_image,\
                                (width-10-(i+1)*life_rect.width,\
                                 height-10-life_rect.height))

        #绘制游戏结束画面
        elif LIFE_NUM == 0:
            pygame.mixer.music.stop()
            pygame.mixer.stop()

            # 停止发放补给
            pygame.time.set_timer(SUPPLY_TIME, 0)

            if not recorded:
                recorded = True
                # 读取历史最高分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
            
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))

            # 绘制结束画面
            record_score_text = score_font.render("Best: %d" % record_score,True,WHITE)
            screen.blit(record_score_text, (50,50))
            
            gameover_text1 = gameover_font.render("Your Score: ", True, WHITE)
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                                (width - gameover_text1_rect.width) // 2, height // 2
            screen.blit(gameover_text1, gameover_text1_rect)

            
            gameover_text2 = gameover_font.render(str(score), True, WHITE)
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                                (width - gameover_text2_rect.width) // 2, \
                                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                        (width - again_rect.width) // 2,\
                        gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                        (width - again_rect.width) // 2, \
                        again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if again_rect.left < pos[0] < again_rect.right and \
                   again_rect.top < pos[1] < again_rect.bottom:
                    main()
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                     gameover_rect.top < pos[1] < gameover_rect.bottom:
                     pygame.quit()
                     sys.exit()

        #画分数
        score_text = score_font.render("Score : %s" % str(score), True, WHITE)
        screen.blit(score_text, (10, 5))

        if not(delay % 10):
            switch_image = not switch_image
            
        #延迟切换我方飞机
        #延迟实际上就是把switch_image变量取反的时间加长了
        delay -= 1
        if not delay:
            delay = 100

        #画暂停
        screen.blit(paused_image, paused_rect)
        
        pygame.display.flip()
        
        clock.tick(60)#每秒60帧

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
