#target 决定去哪个函数执行代码
#args 决定向子线程传递什么参数 要以元祖类型传递
import threading
import time

num = [11,22]
def xiugai(temp):
    print('修改前num = %s' % str(temp))
    temp.append(33)
    print('修改后num = %s' % str(temp))


def printf(temp):
    print('打印现在的 num = %s' % str(temp))


def main():
    t1 = threading.Thread(target=xiugai,args=(num,))
    t2 = threading.Thread(target=printf,args=(num,))
    t1.start()
    time.sleep(1)
    t2.start()

if __name__ == "__main__":
    main()