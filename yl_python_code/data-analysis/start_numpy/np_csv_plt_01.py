import numpy as np
from matplotlib import pyplot as plt

us_file_path = '../youtube_video_data/US_video_data_numbers.csv'
# uk_file_path = '../youtube_video_data/GB_video_data_numbers.csv'

t_us = np.loadtxt(us_file_path, delimiter=',', dtype='int', unpack=False)
# t_uk = np.loadtxt(uk_file_path, delimiter=',', dtype='int', unpack=True)

t_us_comments = t_us[:, -1]
t_us_comments = t_us_comments[t_us_comments <= 5000]   # 发现大于5000的数据极少
# print(t_us_comments)
# print(t_us_comments.max(),t_us_comments.min())

bin_width = 50
# mun_bin = (t_us_comments.max() - t_us_comments.min())//bin_width

# 绘图
plt.figure('直方图', figsize=(20, 8), dpi=80)
plt.hist(t_us_comments, range(t_us_comments.min(), t_us_comments.max()+bin_width, bin_width))
plt.grid(alpha=0.4)
plt.show()
