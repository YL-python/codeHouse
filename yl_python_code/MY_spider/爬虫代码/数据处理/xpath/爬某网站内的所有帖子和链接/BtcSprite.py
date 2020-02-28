import requests
from lxml import etree
import json

class BtsSprite():
    def __init__(self):
        self.url = 'https://www.chainnode.com'
        self.head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
        self.html_num = '/forum/61-{}'

    #请求网络数据
    def Get_url_data(self,num):
        data = requests.get(self.url+self.html_num.format(num),headers = self.head).content.decode()
        return data
    
    #转换格式
    def Get_xpath_data(self,data):
        data = etree.HTML(data)
        return data
    
    #xpath匹配
    def Xpath_pipei(self,data):
        title_list = data.xpath('//h3/a[@class="link-dark-major font-bold bbt-block"]/text()')
        url_list = data.xpath('//h3/a[@class="link-dark-major font-bold bbt-block"]/@href')
        #title = title.replace(' ','')
        data_list= []
        for index,title in enumerate(title_list):
            news = {}
            title = title.replace(' ','')
            title = title.replace('\n','')
            url_list[index] = self.url + url_list[index]
            news['name'] = title
            news['url'] = url_list[index]
            data_list.append(news)
        return data_list 

    #保存
    def Save_data(self,data):
        #调用json方法吧列表转字符串
        data_str = json.dumps(data)
        with open('btc.json','w')as f:
            f.write(data_str)

    
    def Run(self):
        for i in range(1):      #请求页数
            data_str = self.Get_url_data(i)
            data_xpath = self.Get_xpath_data(data_str)
            data_list = self.Xpath_pipei(data_xpath)
            self.Save_data(data_list)
            

if __name__ == "__main__":
    bts = BtsSprite()
    bts.Run()
