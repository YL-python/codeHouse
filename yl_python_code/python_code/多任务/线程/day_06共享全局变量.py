# 子线程共享全局变量
# 创建两个子线程 一个修改 一个打印
import threading
import time

num = 100
def xiugai():
    global num
    print('修改前num = %d' % num )
    num += 100
    print('修改后num = %d' % num)


def printf():
    global num
    print('打印现在的 num = %d' % num)


def main():
    t1 = threading.Thread(target=xiugai)
    t2 = threading.Thread(target=printf)
    t1.start()
    time.sleep(1)
    t2.start()

if __name__ == "__main__":
    main()