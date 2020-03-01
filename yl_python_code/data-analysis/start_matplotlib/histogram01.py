from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=18)
plt.figure('直方图',figsize=(20,8),dpi=80)

a=[131,  98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130, 124, 101, 110, 116, 117, 110, 128, 128, 115,  99, 136, 126, 134,  95, 138, 117, 111,78, 132, 124, 113, 150, 110, 117,  86,  95, 144, 105, 126, 130,126, 130, 126, 116, 123, 106, 112, 138, 123,  86, 101,  99, 136,123, 117, 119, 105, 137, 123, 128, 125, 104, 109, 134, 125, 127,105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120, 114,105, 115, 132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134,156, 106, 117, 127, 144, 139, 139, 119, 140,  83, 110, 102,123,107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133,112, 114, 122, 109, 106, 123, 116, 131, 127, 115, 118, 112, 135,115, 146, 137, 116, 103, 144,  83, 123, 111, 110, 111, 100, 154,136, 100, 118, 119, 133, 134, 106, 129, 126, 110, 111, 109, 141,120, 117, 106, 149, 122, 122, 110, 118, 127, 121, 114, 125, 126,114, 140, 103, 130, 141, 117, 106, 114, 121, 114, 133, 137,  92,121, 112, 146,  97, 137, 105,  98, 117, 112,  81,  97, 139, 113,134, 106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110,105, 129, 137, 112, 120, 113, 133, 112,  83,  94, 146, 133, 101,131, 116, 111,  84, 137, 115, 122, 106, 144, 109, 123, 116, 111,111, 133, 150]

bin_width = 5   # 设置组距
# bin_num = int((max(a) - min(a) )/ bin_width)  # 设置组数  极差/组距

# 组距为5 的时候不能被  （max(a)-min(a)） 整除 绘制出来的图像就会偏移  解决方法是传列表参数让它能被均分
# 实际上就是X轴的最大刻度和最小刻度之差要被 bin_num 均分
plt.hist(a, range(min(a), max(a) + bin_width, bin_width), density=0)   #density=0 频数分布直方图    density=1 频率分布直方图    看源码啦啦啦

# 注意这里X轴的坐标和实际数字的关系 也就是为什么不能被整分的原因
plt.xticks(range(min(a), max(a)+bin_width, bin_width), rotation=45)
plt.xlabel('时长(单位：分)', fontproperties=my_font1)
plt.ylabel('个数', fontproperties=my_font1)
plt.title('电影时长分布情况', fontproperties=my_font1)

# 设置坐标轴显示范围
# plt.xlim(50, 200)
# plt.ylim(0, 300)

plt.grid(alpha=0.4)
plt.show()