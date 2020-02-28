

with open('E:\pycharm\A_Python 总文件\文件操作\\123.txt','r',encoding='UTF-8')as f:
    data = f.readlines()
    for i in data:
        if i is '\n':   # 判空要用 is  之后还可以用正则
            pass
        else:
            with open('E:\pycharm\A_Python 总文件\文件操作\\456.txt','a',encoding='UTF-8')as m:
                m.write(i)