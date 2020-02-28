# 书名 作者 简介 书的图片
import requests
from lxml import etree
from bs4 import BeautifulSoup
import json
import csv

class TushuSprite():
    def __init__(self):
        self.url = 'http://www.allitebooks.com/page/{}/'
        self.head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
        self.data_list = []
    
    #获取所有的 URL
    def Get_url_list(self):
        url_list = []
        for i in range(1,11):
            url = self.url.format(str(i))
            url_list.append(url)
        return url_list

    #发请求
    def Request_url(self, url):
        data = requests.get(url,headers = self.head).content.decode()
        print(url)
        return data

    #bs4解析数据
    def Bs4_data(self,data): 
        data_list = []
        data = BeautifulSoup(data,"lxml")
        bs4_name = data.select('article div header h2 a')
        bs4_by = data.select('article div header div span h5 a')
        bs4_tu_url = data.select('article div a img')
        bs4_jianjie = data.select('article div div p')
        for i in range(10):
            data_dict = {}
            data_dict['姓名'] = bs4_name[i].get_text()
            data_dict['作者'] = bs4_by[i].get_text()
            data_dict['图片'] = bs4_tu_url[i].get('src')
            data_dict['简介'] = bs4_jianjie[i].get_text()
            self.data_list.append(data_dict)
            
    #xpath解析数据
    def Xpath_data(self,data):
        data_list = []
        data = etree.HTML(data)
        xpath_name = data.xpath('//article/div[@class = "entry-body"]/header/h2/a/text()')
        xpath_by = data.xpath('//article/div/header/div/span/h5/a/text()')
        xpath_tu_url = data.xpath('//article/div/a/img/@src')
        xpath_jianjie = data.xpath('//article/div/div/p/text()')
        for i in range(10):
            data_dict = {}
            data_dict['姓名'] = str(xpath_name[i])
            data_dict['作者'] = str(xpath_by[i])
            data_dict['图片'] = str(xpath_tu_url[i])
            data_dict['简介'] = str(xpath_jianjie[i])
            self.data_list.append(data_dict)
        
    #保存数据
    def Save_data(self, data):
        json.dump(data,open("tushu.json","w"))

    def Json_to_csv(self):
        json_fp = open("tushu.json","r",encoding='utf-8')
        csv_fp = open("csv.csv","w",encoding='utf-8')
        data_list = json.load(json_fp)
        sheet_title = data_list[0].keys()
        sheet_data = []
        for data in data_list:
            sheet_data.append(data.values())
        writer = csv.writer(csv_fp)
        writer.writerow(sheet_title)
        writer.writerows(sheet_data)
        json_fp.close()
        csv_fp.close()  
    
    def Run(self):
        url_list = self.Get_url_list()
        for url in url_list:
            data = self.Request_url(url)
            self.Xpath_data(data)
            #self.Bs4_data(data)
        self.Save_data(self.data_list)
        self.Json_to_csv()

if __name__ == "__main__":
    #tushu = TushuSprite()
    #tushu.Run()
    TushuSprite().Run()






























