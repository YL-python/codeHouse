import time
import threading

def changge():
    for i in range(5):
        print("唱歌".center(20,'*'))
        time.sleep(1)





def main():
    print(threading.enumerate())

    t1 = threading.Thread(target=changge)

    print(threading.enumerate())

    t1.start()

    print(threading.enumerate())


if __name__ == '__main__':
    main()

# 在 start 时才创建子线程