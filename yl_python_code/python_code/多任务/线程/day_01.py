import time
import threading
def changge():
    for i in range(5):
        print("我在唱歌".center(20,'*'))
        time.sleep(1)


def tiaowu():
    for i in range(5):
        print("我在跳舞".center(20,'*'))
        time.sleep(1)


def main():
    changge()
    tiaowu()


if __name__ == '__main__':
    main()