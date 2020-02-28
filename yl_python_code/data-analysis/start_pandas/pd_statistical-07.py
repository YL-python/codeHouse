"""
用matplotlib 取排名前十的国家
用matploylib 画中国每个城市店铺的数量
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')
fill_path = "starbucks_store_worldwide.csv"
df = pd.read_csv(fill_path)

# 获取数据
data1 = df.groupby(by='Country')['Brand'].count().sort_values(ascending=False)[:10]
# data2 = df.groupby(by=[df["Country"], df["City"]])['Brand'].count()['CN'].sort_values(ascending=False)[:10]
# print(data1)T
df_CN = df[df['Country']=='CN']
data2 = df_CN.groupby(by='City')  # 是一个DataFrame对象
data2 = data2['Brand'].count().sort_values(ascending=False)[:20]
# print(data2)

_x1 = data1.index
_y1 = data1.values

# 画图
plt.figure(figsize=(10, 6), dpi=80)
plt.bar(range(len(_x1)), _y1, width=0.4)
plt.xticks(range(len(_x1)), _x1)
plt.grid(alpha=0.4)
plt.show()

_x2 = data2.index
_y2 = data2[::-1].values

# 画图
plt.figure(figsize=(6, 10), dpi=80)
plt.barh(range(len(_x2)), _y2, height=0.4)
plt.yticks(range(len(_x2)), _x2[::-1], fontproperties=my_font, fontsize=9)
plt.grid(alpha=0.4)
plt.show()