import pygame
import sys 
# 初始化pygame
pygame.init()

size = width, height = 600, 400
speed = [0,0]
ans = [0,0]
i = 1
bg = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("wasd 和 上下左右 控制方向 空格暂停")

tupianname = pygame.image.load("me1.png")
position = tupianname.get_rect()
position.center = width // 2, height // 2#修改图片起始位置


L_head = tupianname
R_head = pygame.transform.flip(tupianname,True,False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                tupianname = L_head
                speed = [-i,0]
                ans = speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                tupianname = R_head
                speed = [i,0]
                ans = speed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                speed = [0,-i]
                ans = speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                speed = [0,i]
                ans = speed
            if event.key == pygame.K_SPACE:
                if ans == speed:
                    speed=[0,0]
                else:
                    speed = ans
                
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        tupianname = pygame.transform.flip(tupianname,True,False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(tupianname, position)
    pygame.display.flip()
    pygame.time.delay(9)
