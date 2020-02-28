import numpy as np
from matplotlib import pyplot as plt

# 数据 在美国最后加一列0英国最后加一列1 用来区分
us_file_path = '../youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '../youtube_video_data/GB_video_data_numbers.csv'
t_us = np.loadtxt(us_file_path, delimiter=',', dtype='int')
t_uk = np.loadtxt(uk_file_path, delimiter=',', dtype='int')

zeros_data = np.zeros((t_us.shape[0], 1)).astype('int')
ones_data = np.ones((t_uk.shape[0], 1)).astype('int')

t_us = np.hstack((t_us, zeros_data))
t_uk = np.hstack((t_uk, ones_data))

final_data = np.vstack((t_us, t_uk))
print(final_data)
