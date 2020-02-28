import threading
from queue import Queue
import requests
from lxml import etree
import json

CRAWL_EXIT = False
PARSE_EXIT = False

# 采集线程类，继承线程
class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # 调用父类初始化方法
        super(ThreadCrawl, self).__init__()
        # 线程名，页码队列，数据队列
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}


    def run(self):
       print("启动"+self.threadName)
       while not CRAWL_EXIT:
           try:
               # 取出一个页码  false表示队列空了就抛异常//否则是进入阻塞状态
               page = self.pageQueue.get(False)
               url = "http://konachan.net/post?page={}&tags=".format(page)
               data = requests.get(url,headers=self.headers)
               self.dataQueue.put(data)
           except:
               pass
       print("结束" + self.threadName)


#解析线程类，继承线程
class Threadparse(threading.Thread):
    def __init__(self, threadName, dataQueue):
        # 调用父类初始化方法
        super(Threadparse, self).__init__()
        # 线程名，页码队列，数据队列
        self.threadName = threadName
        self.dataQueue = dataQueue


    def run(self):
       print("启动"+self.threadName)
       while not PARSE_EXIT:
           self.dataQueue.get()
       print("结束" + self.threadName)


def main():
    # 页码队列
    pageQueue = Queue(10)
    for i in range(1,11):
        pageQueue.put(i)

    # 网页源码队列
    dataQueue = Queue()

    #线程名字队列
    crawlList = ["采集线程1号", "采集线程2号", "采集线程3号"]

    # 用来存放线程
    threadcrawl = []
    for threadName in crawlList:
        # 实例化线程类对象
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        # 把每个线程对象存到列表里面
        threadcrawl.append(thread)

    parseList = ["解析线程1号", "解析线程2号", "解析线程3号"]
    threadparse = []
    for threadName in parseList:
        # 实例化线程类对象
        thread = Threadparse(threadName, dataQueue)
        thread.start()
        # 把每个线程对象存到列表里面
        threadparse.append(thread)


    while not pageQueue.empty():
        pass
    global CRAWL_EXIT
    CRAWL_EXIT = True
    print("采集队列为空")
    for thread in threadcrawl:
        thread.join()




if __name__ == '__main__':
    main()