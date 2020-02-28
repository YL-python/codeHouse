import os
import re

erroe_name = '\\/:*?"<>|'


def main():
    print("text.....")


def rename(name):
    name = 'aaaa\\/\\:*?"\\<>|aaaa'
    data = re.sub('[/:*?"<>|\\\]', ' ', name)
    print(name)
    print(data)


# 创建文件夹  名称右非法字符的时候替换成空格
def yl_makedirs():
    pass


# 在一个文件夹内递归查找文件  找到返回True 没找到返回False
def findFile(dirs, file):
    flag = False
    for root, dirs, files in os.walk(dirs):
        if files is None:
            continue
        else:
            if file in files:
                flag = True
                break
    return flag


if __name__ == '__main__':
    rename(1)