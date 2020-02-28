"""
不同年份书的数量
不同年份书的平均评分情况
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\simkai.ttf')
fill_path = r'books.csv'
df = pd.read_csv(fill_path)
print(df.info())
# print(df.head(1))

# 不同年份书的数量发现有缺失值
data1 = df[pd.notnull(df['original_publication_year'])]
# print(data1)
group1 = data1.groupby('original_publication_year')['id'].count()
# print(group1)

# 不同年份书的平均评分情况
data2 = df[pd.notnull(df['original_publication_year'])]
group2 = data1['average_rating'].groupby(data2['original_publication_year']).mean()
# print(*zip(group2))
print(group2)

_x = group2.index
_y = group2.values

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x)), _y)
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype('int'), rotation=45)
plt.show()
