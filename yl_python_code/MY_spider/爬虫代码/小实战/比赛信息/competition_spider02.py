import re
import requests
from lxml import etree
import csv


class Competition_spider:

    def __init__(self):
        self.url = 'https://www.jxedu.gov.cn/zt/xzt/jxsdxskjcx/jsfa.htm'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/74.0.3724.8 Safari/537.36'}
        self.data_title = list()
        self.data_url = list()
        self.data_time = list()


    def get_data(self, num):
        data_url = requests.get(self.url.format(num), headers=self.headers)\
            .content.decode("gbk", "ignore")
        # print(data_url)
        return etree.HTML(data_url)

    def xpath_data(self, data):
        data_title = data.xpath(
            '//dl[@class="bbda list_bbda cl"]/dt/a/text()')
        data_url = data.xpath(
            '//dl[@class="bbda list_bbda cl"]/dt/a/@href')
        data_time = data.xpath('//dl[@class="bbda list_bbda cl"]/dd/div/text()')

        for i in range(len(data_url)):
            data_url[i] = data_url[i]
            self.data_url.append(data_url[i])
            self.data_title.append(data_title[i])


    def seava_data(self):
        # print(len(self.data_title))
        # print(len(self.data_title))
        # print(len(self.data_url))
        # print(self.data_cl)
        # print(len(self.data_time))
        # print(len(self.data_look))
        headers = ["标题", "链接", "详情", "发布时间", "浏览量", "图片链接"]
        with open("data.csv", 'w', errors='ignore', newline='')as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            for i in range(len(self.data_url)):
                data = [self.data_title[i], self.data_url[i], self.data_cl[i],
                        self.data_time[i], self.data_look[i], self.data_image[i]]
                f_csv.writerow(data)

    def run(self):
        # 第一步获取网页链接
        for i in range(1, 10):
            print("正在爬取第{}页".format(i))
            xpath_data = self.get_data(i)
            # 第二部解析数据
            self.xpath_data(xpath_data)
        # 保存数据
        self.seava_data()


if __name__ == '__main__':
    spider = Competition_spider()
    spider.run()