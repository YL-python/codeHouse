import pygame
import sys  # 退出程序要用到
# 初始化pygame
pygame.init()

size = width, height = 600, 400
speed = [-2,1]# x轴  y轴 每次增加的大小 
bg = (255, 255, 255) # RGB颜色

# 创建指定大小窗口 调用了 display.set_mode()函数

# 会返回一个 Surface对象 这里赋值给了screen
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("小宝宝，来玩啊!")

# 加载图片
tupianname = pygame.image.load("me1.png")
# 获得图片的位置 矩形
position = tupianname.get_rect()

while True: 
    for even in pygame.event.get():# 事件队列
        if even.type == pygame.QUIT:# 判断事件是不是点击关闭按钮
            sys.exit()      # 退出

    # 移动图像 左上角(0, 0)
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 翻转图片  第一个参数传入对象 第二个参数是否水平翻转
        # 第三个参数是否垂直翻转
        tupianname = pygame.transform.flip(tupianname,True,False)
        # 反向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)# 第九行
    # 显示图片 把图片信息 画 到我们指定大小的窗口上
    screen.blit(tupianname, position)
    # 更新界面 把内存区的图片打到显示屏上
    pygame.display.flip()
    # 延迟 10 毫秒 图片移动速度有一个默认值 设置延迟就是修改这个默认值
    pygame.time.delay(10)

