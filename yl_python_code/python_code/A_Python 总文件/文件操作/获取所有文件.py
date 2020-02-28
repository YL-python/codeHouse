# 获取指定路径下的所有文件名

import os

#  获取指定目录下的  文件或文件夹名称的列表
# filePath = 'D:\学习\认证杯'
# print(os.listdir(filePath))


'''
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
followlinks -- 设置为 true，则通过软链接访问目录。
'''
filePath = 'D:\学习\认证杯'
print('A'.center(50,'*'))
for a,b,c in os.walk(filePath):
    print(a)
print('B'.center(50,'*'))
for a,b,c in os.walk(filePath):
    print(b)
print('C'.center(50,'*'))
for a,b,c in os.walk(filePath):
    print(c)