from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=18)
plt.figure('散点图',figsize=(20,8),dpi=80)

interval = [0,5,10,15,20,25,30,35,40,45,60,90]          # x
width = [5,5,5,5,5,5,5,5,5,15,30,60]     # 组距
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]   # y

plt.bar(range(len(interval)),quantity, width=1)   # 默认宽度是0.8  改为1就会连到一起

# 设置X轴
_x = [i-0.5 for i in range(len(interval)+1)]   # 设置起始点
interval.append(interval[-1]+width[-1])      # 完善 X 的数据
_x_ticks = interval
plt.xticks(_x,_x_ticks)

plt.grid(alpha=0.4)
plt.show()


'''
直方图更适合没有处理过的数据
因为绘制直方图的时候函数内部会处理数据

一般处理好的数据用条形图绘制

这里涉及到了
怎么把条形图连到一起  设置宽度=1 就好了
X轴的设置  plt.xticks([原始X数据的长度]，[实际X的坐标])  
怎么把X轴偏移 让条形图的起始位置在0点   每个数值减半个宽度  0.5
'''