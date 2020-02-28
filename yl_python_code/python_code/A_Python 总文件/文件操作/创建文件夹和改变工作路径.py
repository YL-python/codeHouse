import os

# 小技巧  mkdir 创建已经存在的文件会报错可以用 try-except

with open('text1.txt','w')as f:
    f.write('text1')
# 创建文件夹
os.mkdir("E:\pycharm\A_Python 总文件\文件操作\测试")

with open('text2.txt','w')as f:
    f.write('text2')
# 进入刚刚创建的文件夹
os.chdir("E:\pycharm\A_Python 总文件\文件操作\测试")

with open('text3.txt','w')as f:
    f.write('text3')

# 打印当前工作路径
print(os.getcwd())