'''
2019年8月23日16点50分
读取数据强项不是numpy  是pandas
加载本地文件
第一个参数传文件路径
dalimiter  分隔符 csv文件是 ， 为分隔符
dtype   数据类型
unpack  默认False  每次读取一行   True就是每次读取一列
skiprows   前几行不读取（一般不读取第一行的表头）
usecols   读取哪几列（下表0开始）  可以传整型，元组，列表等  默认none读取所有
'''
import numpy as np

us_file_path = '../youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '../youtube_video_data/GB_video_data_numbers.csv'

t1 = np.loadtxt(us_file_path, delimiter=',',dtype='int',unpack=False,skiprows=2)
t2 = np.loadtxt(us_file_path, delimiter=',',dtype='int',unpack=True,usecols=[1,2,3])
print(t1)
print(t2)
