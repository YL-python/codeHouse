''' 从 matplotlib 库中导入 pyplot 模块并重命名为 plt '''
from matplotlib import pyplot as plt
import random

#  不显示中文-设置字体 方法二
from matplotlib import font_manager
my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=10)
my_font2 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=20)   # 传字体路径   实例化字体对象

# 参数设置
fig = plt.figure(figsize=(20,8),dpi=80)   # 大小和分辨率

# 数据  这里我们绘制10点到12点两个小时的气温变化图
x=range(120)
y=[random.randint(10, 25) for i in range(120)]

# 绘制
plt.plot(x,y)

# 绘制 x y 轴的刻度
_str_x_list = ['10点{}分'.format(i) for i in range(1,60)]
_str_x_list += ['11点{}分'.format(i-60) for i in range(61,120)]
plt.xticks(list(x)[::3],_str_x_list[::3],rotation=45, fontproperties=my_font1)   # 一 一对应 把后面的覆盖到前面的上面   rotation 旋转角度   fontproperties 字体设置

# 添加描述信息
plt.xlabel('时间', fontproperties=my_font2)
plt.ylabel('温度', fontproperties=my_font2)
plt.title('10点到12点温度变化情况', fontproperties=my_font2)

# 保存
# plt.savefig('./t1.png')  # 可以保存为矢量图  .svg  格式

# 表现
plt.show()
