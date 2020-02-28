import threading
import time

# 对于用到相同全局变量的子线程可以用一个锁来控制
# 一个子线程用到全局变量的时候就先锁上 当用完之后再解锁就可以解决资源竞争问题
# 类比上厕所
# 上锁原则 上锁的代码越少越好

num = 0
def test1(temp):
    global num
    # 上锁 如果锁不是锁定转态就上锁成功
    # 如果锁是锁定转态 那就要等这个锁 解锁之后才可以上锁
    for i in range(temp):
        mutex.acquire()
        num += 1
        # 解锁
        mutex.release()
    print('---test1--- num = %d' % num)


# 创建锁
mutex = threading.Lock()


def test2(temp):
    global num
    for i in range(temp):
        mutex.acquire()
        num += 1
        mutex.release()
    print('---test2--- num = %d' % num)


def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(2)
    print('---main--- num = %d' % num)

if __name__ == "__main__":
    main()