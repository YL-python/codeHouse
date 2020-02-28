# -*- coding:utf-8 -*-
import os
import winsound

import yl_tool

# 需要知道 输入/输出 的文件名称
# 获取到文件列表
ts_file_path = 'F:\\obb\\新建文件夹\\'
ts_file_name = 'Y2hlbmppbmdjb25n'
out_path = 'F:\\obb\\A{}.ts'


# 把 input_file_name 文件复制到 output_file_name
def ts2mp4(input_file_name, output_file_name):
    with open(input_file_name, "rb") as _in:
        data = _in.read()
    with open(output_file_name, "ab+")as output:
        output.write(data)


def main():
    dir_list = os.listdir(ts_file_path)
    for dir in dir_list:
        print("\n正在处理 {} 文件夹".format(dir))
        ts_dir = os.path.join(ts_file_path, dir)
        ts_file_num = len(os.listdir(ts_dir))
        for i in range(ts_file_num):
            yl_tool.progress_bar(i, ts_file_num - 1, text="合成中: {}".format(dir))
            input_file_name = os.path.join(ts_dir, ts_file_name+str(i))
            output_file_name = out_path.format(dir[0:9])
            # print(input_file_name,output_file_name)
            ts2mp4(input_file_name, output_file_name)
    # 完成提示音
    winsound.Beep(600, 500)


if __name__ == '__main__':
    main()
