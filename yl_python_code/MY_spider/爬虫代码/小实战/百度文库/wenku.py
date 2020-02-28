import requests
import time
import json
import re


class wenku_spider():
    def __init__(self,wenku_url):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"}
        self.v_url = 'http://wenku.baiduvvv.com/doc/'
        self.url_one = 'http://wenku.baiduvvv.com/ds.php?url={}&type=doc&t={}&sign={}'
        self.url_two = '{}/wkc.php?url={}&type=doc&t={}&sign={}&f={}&h={}&btype=start&callback=callback2&_={}'
        self.wenku_url = wenku_url
        self.vars = {
            't': '',
            'sign': '',
            's': '',
            'f': '',
            'h': ''
        }

    def get_t_sign(self):
        data = requests.get(url=self.v_url, headers=self.headers).content.decode('utf-8')
        '<input type="hidden" name="sign" value="5d2bfffed8f25049249bcd26ffc2f6e9" />'
        t_re = re.compile('<input type="hidden" name="t" value="(.*?)" />',re.S)
        sign_re = re.compile('<input type="hidden" name="sign" value="(.*?)" />', re.S)
        t = t_re.findall(data)
        sign = sign_re.findall(data)
        self.vars['t'] = t[0]
        self.vars['sign'] = sign[0]

    def requests_one(self):
        url = self.url_one.format(self.wenku_url,self.vars['t'],self.vars['sign'])
        data = requests.get(url,headers=self.headers).content.decode('utf-8')
        data = json.loads(data)
        self.vars['s'] = data['s']
        self.vars['f'] = data['f']
        self.vars['h'] = data['h']

    def requests_two(self):
        time_var = int(time.time()*1000)
        url = self.url_two.format(self.vars['s'], self.wenku_url, self.vars['t'],self.vars['sign'],self.vars['f'],self.vars['h'],time_var)
        print(url)
        # data = requests.get(url, headers=self.headers)

    def Run(self):
        # konachan_spider 获取sign 和t的值
        self.get_t_sign()
        # wallhaven_spider 网页的第1步请求 获取下载地址和f,h,s参数
        self.requests_one()
        # 3 网页的第2步 获取did和id参数   code=2表示可以直接请求下载  不然就是带着did  id参数去解析之后在下载
        self.requests_two()


if __name__ == '__main__':
    wemku_url = 'https://wenku.baidu.com/view/02c4678969dc5022aaea0072.html?from=search'
    wenku = wenku_spider(wemku_url)
    wenku.Run()
