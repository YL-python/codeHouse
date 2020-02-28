#target 决定去哪个函数执行代码
#args 决定向子线程传递什么参数 要以元祖类型传递
import threading
import time

num = 0
def test1(temp):
    global num
    for i in range(temp):
        num += 1
    print('---test1--- num = %d' % num)


#cpu执行的时间内 某个子线程没有执行完就去执行另外一个子线程了


def test2(temp):
    global num
    for i in range(temp):
        num += 1
    print('---test2--- num = %d' % num)



def main():
    t1 = threading.Thread(target=test1,args=(10000000,))
    t2 = threading.Thread(target=test2,args=(10000000,))
    t1.start()
    t2.start()
    time.sleep(3)
    print('---main--- num = %d' % num)

if __name__ == "__main__":
    main()