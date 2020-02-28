'''
用bool索引筛选数据
'''

import numpy as np
from matplotlib import pyplot as plt

# 数据
uk_file_path = '../youtube_video_data/GB_video_data_numbers.csv'
t_uk = np.loadtxt(uk_file_path, delimiter=',',  dtype='int')
t_uk = t_uk[t_uk[:, 1] <= 500000]
t_uk_comment = t_uk[:, -1]
t_uk_like = t_uk[:, 1]

# 绘图
plt.figure('散点图', figsize=(20, 8), dpi=80)
plt.scatter(t_uk_like, t_uk_comment)
plt.grid(alpha=0.4)
plt.show()
