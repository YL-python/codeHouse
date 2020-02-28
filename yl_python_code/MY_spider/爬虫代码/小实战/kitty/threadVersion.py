from threading import Thread
from lxml import etree
from fake_useragent import UserAgent
import requests
from queue import Queue

web = 'https://www.915cf.com'
message = []


def queue_url(page):
    q = Queue()
    for i in range(1, page + 1):
        link = web + '/shipin/list-%E4%BA%9A%E6%B4%B2%E6%97%A0%E7%A0%81-{0}.html'.format(i)
        # link = web + '/shipin/list-%E7%9F%AD%E8%A7%86%E9%A2%91-{0}.html'.format(i)
        q.put(link)
    return q


class CrawlInfo(Thread):
    def __init__(self, queue_web):
        super().__init__()
        self.ua = UserAgent()
        self.queue_web = queue_web

    def run(self):
        header = {'User-Agent': self.ua.random}
        while not self.queue_web.empty():
            response = requests.get(url=self.queue_web.get(), headers=header)
            response.encoding = 'utf-8'
            e = etree.HTML(response.text)
            xpath = e.xpath('//*[@id="tpl-img-content"]/li/a')
            #  xpath = e.xpath('//*[@id="grid"]/li/a')
            for x in xpath:
                href = x.attrib.get('href')
                title = x.attrib.get('title')
                try:
                    thunder_web = requests.get(url=web + href, headers=header)
                    e = etree.HTML(thunder_web.text)
                    x = e.xpath('//*[@id="downlist1"]/table/tbody/tr[2]/td[2]/a[1]')
                    thunder = x[0].attrib.get('href')
                    m = (web + href, '\t' + title + '\t', thunder + '\n')
                    print(m)
                    message.append(m)
                except e:
                    print(e)


# 保存
def store():
    f = open(file='./kitty1.txt', mode='a', encoding='utf-8')
    for m in message:
        f.writelines(m)
    f.flush()
    f.close()


if __name__ == '__main__':
    queue_link = queue_url(25)
    c = []
    for _ in range(15):
        crawl = CrawlInfo(queue_link)
        c.append(crawl)
        crawl.start()
    for stop in c:
        stop.join()
    store()
