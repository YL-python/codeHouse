'''
2019年8月24日09点36分
numpy 索引和切片   索引除了xpath都是从0开始

t1[ 行,列 ]   取所有用 ：    取不连续用 [] 列表   取连续可以用  x:y:z  形式   x:  表示取x之后的所有的

x:y   值取不到y  表示[x,y)  值是 [x,y-1]   注意这个 和索引从0开始

'''
import numpy as np

us_file_path = '../youtube_video_data/US_video_data_numbers.csv'
uk_file_path = '../youtube_video_data/GB_video_data_numbers.csv'

t1 = np.loadtxt(us_file_path, delimiter=',',dtype='int')
# t2 = np.loadtxt(uk_file_path, delimiter=',',dtype='int')
print(t1)
# print(t2)
print('*'*20)
# 取行
print(t1[0])
print('*'*20)
# 取多行
print(t1[0:6])
print('*'*20)
print(t1[ [2,5,7] ])
print(t1[0:6])
print('*'*20)

# 取3行四列的值
a = t1[2,3]
print(a)
print(type(a))