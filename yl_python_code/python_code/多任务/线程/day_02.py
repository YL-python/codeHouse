import time
import threading

class A:
    def changge():
        for i in range(100):
            print("唱歌".center(20,'*'))
            time.sleep(1)


def tiaowu():
    for i in range(100):
        print("我在跳舞".center(20,'*'))
        time.sleep(1)


def main():
    t1 = threading.Thread(target=A.changge)
    t2 = threading.Thread(target=tiaowu)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()