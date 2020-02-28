# 查看进程数
import time
import threading

def changge():
    for i in range(5):
        print("唱歌  %d".center(20,'*') % i )
        time.sleep(1)


def tiaowu():
    for i in range(10):
        print("我在跳舞  %d".center(20,'*') % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=changge)
    t2 = threading.Thread(target=tiaowu)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)

if __name__ == '__main__':
    main()