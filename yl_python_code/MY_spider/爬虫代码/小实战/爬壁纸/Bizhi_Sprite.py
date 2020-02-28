import requests
import re

class BizhiSprite:
    def __init__(self):
        self.url = 'http://www.netbian.com/desk/{}-1920x1080.htm'
        self.head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

    def Get_url(self,url):
        r = requests.get(url,headers = self.head)
        return r.content

    def Get_bizhi(self,r):
        data = []
        p = re.compile('<img src="(http://\S*.jpg)"')
        data = p.findall(r)
        return data[1]

    def Save_bizhi(self,data,num):
        with open("{}.jpg".format(num+21611),"wb")as f:
            f.write(data)

    def Run(self):
        #konachan_spider.来一个205的循环保存 速度可以控制
        #wallhaven_spider.先生成对应的网页
        #3.请求数据
        #4.正则表达式处理数据得到想要的网站
        #5.请求数据并保存数据
        for i in range(200):
            try:
                url = self.url.format(i+21611)
                print(url)
                r = self.Get_url(url).decode('gbk')
                bizhi = self.Get_bizhi(r)
                print(bizhi)
                bizhi_data = self.Get_url(bizhi)
                self.Save_bizhi(bizhi_data,i)
            except IndexError:
                pass
        
if __name__=='__main__':
    bizhi = BizhiSprite()
    bizhi.Run()
