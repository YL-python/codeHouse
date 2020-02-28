# 获取某个路径下所有文件夹名称
# import os
# print(os.listdir(r'E:\pycharm\多任务\text'))
import os
import multiprocessing


def copy_fill(q,fill_name,old_fill_path,new_fill_path):
    # print("正在复制%s---->%s " % (old_fill_path+fill_name,new_fill_path+fill_name))
    old_f = open(old_fill_path + '\\' + fill_name,'rb')
    new_f = open(new_fill_path +'\\' + fill_name, 'wb')
    fill = old_f.read()
    new_f.write(fill)
    old_f.close()
    new_f.close()
    # 拷贝完成时向队列里面加一个消息表示完成了
    q.put(fill_name)

def main():
    # 1、复制要copy文件夹的路径
    old_fill_path = 'E:\pycharm\多任务\进程测试文件'

    # 2、创建一个新文件夹
    new_fill_path = '进程测试文件[副本]'
    try:
        os.mkdir(new_fill_path)
    except:
        pass

    # 3、获取旧文件夹里面所有文件名称
    old_fill_list = os.listdir(old_fill_path)
    # 4、创建进程池 和 消息队列
    q = multiprocessing.Manager().Queue()
    po = multiprocessing.Pool(5)

    for fill_name in old_fill_list:
        po.apply_async(copy_fill,args=(q,fill_name,old_fill_path,new_fill_path))

    all_fill_num = len(old_fill_list)
    copy_ok_num = 0
    po.close()
    # po.join()
    # 多进程的时候不会报错 有错误就直接跳过
    while True:
        q.get()
        copy_ok_num+=1
        print('\r拷贝的进度 %.2f %%' % (copy_ok_num*100/all_fill_num), end='')
        if copy_ok_num == all_fill_num:
            break

if __name__ == "__main__":
    main()