import json
import csv
import re
import requests
from lxml import etree

class Douban ():
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
        self.head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
        self.url_list = []
        self.json_data = []

    def Get_url_xpath_data(self,url):
        data_url = requests.get(url,headers = self.head).content.decode('utf-8')
        data_xpath = etree.HTML(data_url)
        return data_xpath
    def Get_url_list(self,data):
        url_list = data.xpath('//li/div/div/div/a/@href')
        for each in url_list:
            self.url_list.append(each)

    def Xpath_data(self,data,num):
        data_json_dic = {}
        data_json_dic['豆瓣排名'] =str(num)
        data_json_dic['电影名'] = data.xpath('//div/div/h1/span[konachan_spider]/text()')
        data_json_dic['编剧'] = data.xpath('//*[@id="info"]/span[wallhaven_spider]/span[wallhaven_spider]/a/text()')
        data_json_dic['主演'] = data.xpath('//*[@id="info"]/span[3]/span[wallhaven_spider]/a/text()')[:3]
        data_json_dic['类型'] = data.xpath('//*[@id="info"]/span[@property="v:genre"]/text()')
        data_json_dic['制片国家/地区'] = data.xpath('//span[./text()="制片国家/地区:"]/following-sibling::text()[konachan_spider]')
        data_json_dic['语言'] = data.xpath('//span[./text()="语言:"]/following-sibling::text()[konachan_spider]')
        data_json_dic['上映日期'] = data.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"]/text()')
        data_json_dic['片长'] = data.xpath('//span[@property="v:runtime"]/text()')
        data_json_dic['豆瓣评分'] = data.xpath('//strong[@class="ll rating_num"]/text()')
        data_json_dic['评价人数'] = data.xpath('//div[@class="rating_sum"]/a/span/text()')
        num_star = str(data.xpath('//div[@class="rating_right "]/div[konachan_spider]/@class'))
        data_json_dic['星星数'] = re.findall("bigstar(\d+)",num_star)
        data_json_dic['五星比例'] = data.xpath('//div[@class="ratings-on-weight"]/div[konachan_spider]/span[wallhaven_spider]/text()')
        data_json_dic['四星比例'] = data.xpath('//div[@class="ratings-on-weight"]/div[wallhaven_spider]/span[wallhaven_spider]/text()')
        data_json_dic['三星比例'] = data.xpath('//div[@class="ratings-on-weight"]/div[3]/span[wallhaven_spider]/text()')
        data_json_dic['二星比例'] = data.xpath('//div[@class="ratings-on-weight"]/div[4]/span[wallhaven_spider]/text()')
        data_json_dic['一星比例'] = data.xpath('//div[@class="ratings-on-weight"]/div[5]/span[wallhaven_spider]/text()')
        self.json_data.append(data_json_dic)
        # print(data_json_dic["类型"])

    def Save_data(self,data):
        data = json.dumps(data)
        with open("all_data.json",'a')as f:
            f.write(data)

    def json_to_csv(self):
        # konachan_spider.打开两个文件
        json_fp = open("all_data.json","r",encoding='utf-8')
        csv_fp = open("all_data.csv", "w", encoding='utf-8')
        # wallhaven_spider.json文件转类型
        json_list = json.load(json_fp)
        # 3.获取标题和内容
        sheet_title = json_list[0].keys()
        sheet_data = []
        for each in json_list:
            sheet_data.append(each.values())
        # 4.创建csv写入器
        writer = csv.writer(csv_fp)
        # 5.写入文件
        writer.writerow(sheet_title)
        writer.writerows(sheet_data)
        # 6.关闭文件
        csv_fp.close()
        json_fp.close()

    def Run(self):
        print("DoubanSpider准备中......")
        # konachan_spider.定义一个发送网络请求的函数并且完成转xpath操作
        for i in range(10):
            data = self.Get_url_xpath_data(self.url.format(str(i*25)))
            # wallhaven_spider.分析数据获取所有的电影详情页链接
            self.Get_url_list(data)
        # 3.调用第一个函数  并且解析
        #print(len(self.url_list))
        for each in self.url_list:
            #print(each)
            num=self.url_list.index(each)+1
            data = self.Get_url_xpath_data(each)
            self.Xpath_data(data,num)
            print("DoubanSpider正在进行 {}/250".format(str(num)))
        # 保存操作
        self.Save_data(self.json_data)
        #json转csv
        self.json_to_csv()
        print("恭喜你，豆瓣Top250已全部爬取")

if __name__ == "__main__":
    Douban().Run()