import pygame
import sys  # 退出程序要用到
# 初始化pygame
pygame.init()

bg=(0, 0, 0)#背景颜色
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("把事件显示到屏幕上")

#定义字体对象 font
font = pygame.font.Font(None, 20)
#获取font字体高度
line_height = font.get_linesize()
position=0

screen.fill(bg)#用bg去刷屏幕

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        #render把文本渲染成图像信息 文本 是否消去字体锯齿 颜色
        #blit打印图片 0是x轴起始位置 position是y轴起始位置
        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)
            


    pygame.display.flip()
