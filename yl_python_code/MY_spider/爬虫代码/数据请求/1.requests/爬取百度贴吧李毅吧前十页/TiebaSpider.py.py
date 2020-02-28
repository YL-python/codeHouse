#现在开始爬虫最好都写成面向对象
import requests

class TiebaSpider:
    def __init__(self,tieba_name):#初始化
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

    def get_url_list(self):#获取需要访问的网页列表
        '''
        url_list = []
        for i in range(10):
            url_list.append(self.url_temp.format(i*50))
        return url_list
        非主流方法
        '''
        return [self.url_temp.format(i*50) for i in range(10)]#列表推导式 主流
    
    def parse_url(self,url):#请求网页
        print(url)
        response = requests.get(url,headers = self.head)
        return response.content.decode("utf-8")

    def save_html(self,html_str,page_num):#保存网页
        file_name = "{}-第{}页.html".format(self.tieba_name,page_num)
        with open(file_name,"w",encoding = "utf-8") as f: #对齐相应编码 encode编码
            f.write(html_str)
    
    def run(self):#实现主要逻辑  先写思路在写代码
        #生成URL列表
        url_list = self.get_url_list()
        for url in url_list:
            #遍历，发送请求，获取响应
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1 #获取页码数
            #保存
            self.save_html(html_str,page_num)

if __name__ == "__main__":
    tieba_spider = TiebaSpider("李毅")#实例化对象
    tieba_spider.run()# 调用方法
