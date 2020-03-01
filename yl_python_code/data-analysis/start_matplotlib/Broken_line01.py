''' 从 matplotlib 库中导入 pyplot 模块并重命名为 plt '''
from matplotlib import pyplot as plt
import random

# 参数设置
fig = plt.figure(figsize=(20, 8), dpi=80)  # 大小和分辨率

x = range(2, 26, 2)
y = [random.randint(10, 25) for i in range(12)]

# 绘制
plt.plot(x, y)

# 绘制 x y 轴的刻度
_xticks_list = [i / 2 for i in range(0, 49)]
_yticks_list = range(min(y), max(y) + 1)
plt.xticks(_xticks_list[::3])  # 传啥  X轴就绘制啥
plt.yticks(_yticks_list)

# 保存
# plt.savefig('./t1.png')  # 可以保存为矢量图  .svg  格式

# 表现
plt.show()
