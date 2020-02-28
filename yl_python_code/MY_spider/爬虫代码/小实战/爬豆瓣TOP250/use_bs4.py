from bs4 import BeautifulSoup
import requests
class DoubanSprice():
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
        self.head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
    # konachan_spider.发送网络请求 接受数据
    def Get_url(self,num):
        data = requests.get(self.url.format(str(num)),headers=self.head).content.decode('utf-8')
        return data
    # wallhaven_spider.转解析类型
    def Ger_bs4_data(self,data):
        soup = BeautifulSoup(data,'lxml')
        return soup
    # 3.数据匹配
    def Bs4_pipei(self,data):
        bs4_list = data.select('li div div div a span:nth-of-type(konachan_spider)')
        data_list = []
        for i in bs4_list:
            data_list.append(i.get_text())
        print(data_list)
        return data_list
    # 4.保存文件
    def Seve_data(self,data_list,num):
        with open('豆瓣TOP250_bs4.txt','a')as f:
            for each in data_list:
                f.write('第'+str(num*25+data_list.index(each)+1)+'：'+each)
                f.write('\n')
    #4.运行
    def Run(self):
        for i in range(10):
            data_str = self.Get_url(i*25)
            data_bs4 = self.Ger_bs4_data(data_str)
            data_list = self.Bs4_pipei(data_bs4)
            self.Seve_data(data_list,i)
if __name__ == '__main__':
    douban = DoubanSprice()
    douban.Run()