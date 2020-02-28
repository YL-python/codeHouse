# 进程的交互是用队列来实现   from multiprocessing import Queue
# q.get()          出队
# q.put()          入队
# q.full()         判断队满 满返回TRUE
# q.empty()        判断队空 空返回TRUE
# q.get_nowait()   出队 队空出队报错
# q.put_nowait()   入队 队满入队报错
# 不能用于主进程和进程池之间的通信

import multiprocessing

def download_data(q):
    data = [11,22,33,44]
    for temp in data:
        q.put(temp)
    print('数据下载成功')

def chuli_data(q):
    data = list()
    while True:
        q_data = q.get()
        data.append(q_data)
        if q.empty():
            break
    print(data)

def main():
    q = multiprocessing.Queue()   # 创建队列 传参表示队列最大容量 不传默认最大

    p1 = multiprocessing.Process(target = download_data,args=(q,))
    p2 = multiprocessing.Process(target=chuli_data,args=(q,))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()