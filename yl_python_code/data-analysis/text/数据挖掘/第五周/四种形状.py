import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure(1)  # 创建第一个画板

# 绘制条形图
plt.subplot(221)  # 分成2*2，占用第一个，即第一行第一列的子图
plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="one")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="two", color='g')
plt.legend()
plt.title(u'条形图')

# 绘制直方图
plt.subplot(222)  # 分成2*2，占用第二个，即第一行第二列的子图
population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65,
                   54, 44, 43, 42, 48]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(population_ages, bins, histtype='bar', label='age', rwidth=0.8)
plt.legend()
plt.title(u'直方图')

# 绘制散点图
plt.subplot(223)  # 分成2*2，占用第三个，即第二行第一列的子图
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]
plt.scatter(x, y, label='skitscat', color='k', s=25, marker="o")
plt.legend()
plt.title(u'散点图')

# 绘制饼图
plt.subplot(224)  # 分成2*2，占用第四个，即第二行第二列的子图
slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')
plt.legend()
plt.title(u'饼图')

plt.show()
