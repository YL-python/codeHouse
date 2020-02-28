# 把类变成线程
import threading
import time

class MyThread(threading.Thread):

    def run(self):
        for i in range(3):
            time.sleep(1)
            print('调用了%d次类' % i)


if __name__ == "__main__":
    t = MyThread()
    t.start()

# 创建的类要继承 threading.Thread
# 类里面一定要有run方法
# 调用子线程时要用 start 方法