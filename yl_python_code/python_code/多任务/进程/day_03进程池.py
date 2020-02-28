import multiprocessing
import os,time,random

def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,'执行完毕，耗时%0.2f' % (t_stop-t_start))

po = multiprocessing.Pool(3)   # 创建进程池 表示最大能执行进程数

for i in range(0,10):
    # 向进程池里面传递进程 只是传递 先传递 完了之后再排队按进程池大小来执行进程
    po.apply_async(worker,(i,))

print('___start___')
po.close()   # 关闭进程池
po.join()   # 等待进程池里面所有进程完成
print('___end___')