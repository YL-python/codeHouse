import os


def file_rename(root, del_name):
    for directory, subdir_list, file_list in os.walk(root):
        for name in subdir_list:
            # 当前所在的文件夹
            # print(os.path.join(directory, name))
            old_name = os.path.join(directory, name)
            new_name = old_name.replace(del_name, "")
            os.rename(old_name, new_name)
        for name in file_list:
            old_name = os.path.join(directory, name)
            new_name = old_name.replace(del_name, "")
            os.rename(old_name, new_name)


if __name__ == '__main__':
    file_path = 'E:\A 视频教程\A 前端\慕课网-黄奕Vue-饿了么项目一二期'
    del_name = '--【IT视频学习网-www.itspxx.com】'
    file_rename(file_path, del_name)
