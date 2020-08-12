import datetime
import os

root = '%s%s%s' % ('..', os.path.sep, '文件操作')
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        source_name = '%s%s%s' % (directory, os.path.sep, name)
        timestamp = os.path.getmtime(source_name)  # 获取文件建立的时间戳
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')  # 把时间戳转换成标准时间形式
        target_name = '%s%s%s_%s' % (directory, os.path.sep, modified_date, name)

        print('Renaming: %s to: %s' % (source_name, target_name))

        # os.rename(source_name, target_name)   #  重命名函数
