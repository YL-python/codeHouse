'''
所谓蒙特卡洛的数值计算方法就是：将对某个值的计算为概率，而概率的计算（刚好利用计算机的计算优势）转换为大量随机数的分布情况。
这里用蒙特卡洛方法近似计算  PI 的值
'''
import random
cnt = 0
item = 3000000
for i in range(item):
    x = random.random()
    y = random.random()
    if x**2 + y**2 < 1 :
        cnt = cnt + 1
print(4*cnt/item)
