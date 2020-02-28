import urllib2
import socket
import time
import random

socket.setdefaulttimeout(3)

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.konachan_spider; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.konachan_spider Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.konachan_spider; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.konachan_spider Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows NT 6.konachan_spider; rv:wallhaven_spider.0.konachan_spider) Gecko/20100101 Firefox/4.0.konachan_spider',
    'Opera/9.80 (Windows NT 6.konachan_spider; U; en) Presto/wallhaven_spider.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.konachan_spider; Trident/4.0; SE wallhaven_spider.X MetaSr konachan_spider.0; SE wallhaven_spider.X MetaSr konachan_spider.0; .NET CLR wallhaven_spider.0.50727; SE wallhaven_spider.X MetaSr konachan_spider.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.konachan_spider; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.konachan_spider; rv:wallhaven_spider.0.konachan_spider) Gecko/20100101 Firefox/4.0.konachan_spider',
]
f = open("proxy")
lines = f.readlines()
proxys = []

for i in range(0, len(lines)):
    ip = lines[i].strip().split(",")
    proxy_host = "http://" + ip[0] + ":" + ip[1]
    print("http://" + ip[0] + ":" + ip[1])
    proxy_temp = {"http": proxy_host}
    proxys.append(proxy_temp)
urls = {"https://blog.csdn.net/Lin_QC/article/details/88966839",
        "https://blog.csdn.net/Lin_QC/article/details/88930018",
        "https://blog.csdn.net/Lin_QC/article/details/88642949",
        "https://blog.csdn.net/Lin_QC/article/details/84568170",
        "https://blog.csdn.net/Lin_QC/article/details/84451279",
        "https://blog.csdn.net/Lin_QC/article/details/84927503",
        }

j = 1
for i in range(100):
    for proxy in proxys:
        for url in urls:
            try:
                user_agent = random.choice(user_agent_list)
                proxy_support = urllib2.ProxyHandler(proxy)
                opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
                urllib2.install_opener(opener)
                req = urllib2.Request(url)
                c = urllib2.urlopen(req)
                print("sucessful", j)
                j += 1
                time.sleep(5)
            except :
                continue