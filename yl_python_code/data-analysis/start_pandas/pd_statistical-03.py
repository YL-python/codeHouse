"""
统计电影分类情况
定义一个全为0的数组 列明为类名  数据中出现一次加一

# pd.set_option('display.max_columns', 1000)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_colwidth', 1000)

"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

fill_path = r'./IMDB-Movie-Data.csv'
df = pd.read_csv(fill_path)
# print(df.info())
# print(df.head(1))

# 统计分类的列表
genre_list = df['Genre'].str.split(',').tolist()
genre_list_set = list(set(i for j in genre_list for i in j))

# # 构造全为0 的一维数组
# genre_zero = pd.Series(np.zeros(len(genre_list_set)),
#                           index=genre_list_set, dtype=int)
# # 给每个电影出现分类的赋值
# for i in genre_list:
#     genre_zero[i] += 1
# print(genre_zero)

# 构造全为0 的二维数组
genre_zero = pd.DataFrame(np.zeros((df.shape[0], len(genre_list_set))),
                          columns=genre_list_set)
# 给每个电影出现分类的赋值
for i in range(df.shape[0]):
    genre_zero.loc[i, genre_list[i]] = 1
sum_genre = genre_zero.sum(axis=0)
count_genre = sum_genre.sort_values()
print(count_genre)

# print(genre_zero)

# 画图
plt.figure(figsize=(10, 6), dpi=80)
_x = count_genre.index
_y = count_genre.values
plt.bar(_x, _y)
plt.xticks(_x, rotation=45)
plt.grid(alpha=0.4)
plt.show()
