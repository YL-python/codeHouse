"""
rating，runtime的分布情况
"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf',
                                      size=18)
fill_path = r'./IMDB-Movie-Data.csv'
df = pd.read_csv(fill_path)
# print(df.info())
# print(df.head(1))

# rating runtime分布情况 - 直方图
runtime_data = df['Runtime (Minutes)'].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

rating_data = df['Rating'].values
max_rating = rating_data.max()
min_rating = rating_data.min()
# print(min_rating, max_rating)

# 绘图
plt.figure('电影时常和评分统计表', figsize=(10, 6), dpi=80)

ax1 = plt.subplot(2, 1, 1)
runtime_bin_width = 5
runtime_bin_num = range(min_runtime, max_runtime
                        + runtime_bin_width, runtime_bin_width)
plt.hist(runtime_data, runtime_bin_num)
plt.xticks(runtime_bin_num)
plt.xlabel('时长(单位：分)', fontproperties=my_font, fontsize=9)
plt.ylabel('个数(单位：个)', fontproperties=my_font, fontsize=9)
plt.grid(alpha=0.4)
ax1.set_title("电影时常统计表", fontproperties=my_font)

ax2 = plt.subplot(2, 1, 2)
rating_bin_width = 0.5
# 构造组数 组距是小数的时候就不能用range函数  一样是(min, max+bin_width, bin_width)
rating_bin_num = []
i = min_rating
while i <= max_rating+rating_bin_width:
    rating_bin_num.append(i)
    i += rating_bin_width
# print(rating_bin_num)
plt.hist(rating_data, rating_bin_num)
plt.xticks(rating_bin_num)
plt.xlabel('评分(单位：分)', fontproperties=my_font, fontsize=9)
plt.ylabel('个数(单位：个)', fontproperties=my_font, fontsize=9)
# plt.ylim(0,5)
plt.grid(alpha=0.4)
ax2.set_title("电影评分统计表", fontproperties=my_font)

# 调整每隔子图之间的距离
plt.tight_layout(1.1)
plt.show()

# 设置两个画板
# plt.figure(1)
# plt.figure(2)
