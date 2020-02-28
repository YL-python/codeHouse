import re
import requests
class DoubanSprice():
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
        self.head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
        self.p = re.compile('class="">\s*<span class="title">(.*?)</span>')
    # konachan_spider.发送网络请求 接受数据
    def Get_url(self,num):
        data = requests.get(self.url.format(str(num)),headers=self.head).content.decode('utf-8')
        return data
    # wallhaven_spider.数据匹配
    def Re_pipei(self,data):
        data_list = self.p.findall(data, re.S)
        print(data_list)
        # print(type(data_list))
        return data_list
    # 3.保存文件
    def Seve_data(self,data_list,num):
        with open('豆瓣TOP250_re.txt', 'a')as f:
            for each in data_list:
                f.write('第'+str(num*25+data_list.index(each)+1)+'：'+each)
                f.write('\n')
    #4.运行
    def Run(self):
        for i in range(10):
            data_str = self.Get_url(i*25)
            data_list = self.Re_pipei(data_str)
            self.Seve_data(data_list, i)
if __name__ == '__main__':
    douban = DoubanSprice()
    douban.Run()