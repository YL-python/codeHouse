# -*- coding:utf-8 -*-
# 参数
# ts文件路径
# ts文件名称
# ts文件个数
# 输出路径
import os
import yl_tool
import winsound

file_name = "ee291370918d8065ba494321b5f5e9bb4b358d70"
ts_file_name = 'Y2hlbmppbmdjb25n'
ts_file_path = 'F:\\obb\\新建文件夹\\{}\\'.format(file_name)
out_path = 'F:\\obb\\A{}.ts'.format(file_name[0:9])

num = len(os.listdir(ts_file_path)) + 1

for i in range(num):
    # print("\r正在处理第{}个文件".format(i), end="")
    yl_tool.progress_bar(i, num-1, text="合成中...")
    file = ts_file_path + ts_file_name + str(i)
    try:
        with open(file.format(i), "rb") as _in:
            data = _in.read()
        with open(out_path, "ab+")as output:
            output.write(data)
    except FileNotFoundError:
        print("\n操作完成")
        break

# 其中600表示声音大小，500表示发生时长，500为1秒
winsound.Beep(600, 500)