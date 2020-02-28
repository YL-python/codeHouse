# -*- coding:utf-8 -*-


# file_name = "F:\\obb\\新建文件夹\\8cd00b941bedc5e3ebad82472f274bc2c159d1c6\\Y2hlbmppbmdjb25n{}"
#
# for i in range(472):
#     print(i)
#     with open(file_name.format(i), "rb") as f:
#         x = f.read()
#     with open("F:\\obb\\1", "ab+")as f1:
#         f1.write(x)

# import winsound
# winsound.Beep(600,500)

import time
import shutil

file_name = "D:\\Desktop\\新建文件夹\\python\\A12f4e3bf5.ts"
file = "D:\\Desktop\\新建文件夹\\A12f4e3bf5.ts"

start_time = time.time()

with open(file, "rb") as _in:
    data = _in.read()
with open(file_name, "ab+")as output:
    output.write(data)

end_time = time.time()

print(end_time - start_time)