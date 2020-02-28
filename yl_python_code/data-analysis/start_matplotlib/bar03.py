from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=12)
plt.figure('条形图',figsize=(20,8),dpi=80)

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

bar_width = 0.2

x_14 = range(len(a))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

plt.bar(x_14, b_14, width=bar_width, label='14日')
plt.bar(x_15, b_15, width=bar_width, label='15日')
plt.bar(x_16, b_16, width=bar_width, label='16日')

plt.ylabel('票房',fontproperties=my_font1)
plt.xlabel('日期',fontproperties=my_font1)
plt.title('三大电影三天票房对比',fontproperties=my_font1)

plt.xticks(x_15,a,fontproperties=my_font1)

plt.plot()
plt.grid(alpha=0.4)
plt.legend(prop=my_font1)
plt.show()