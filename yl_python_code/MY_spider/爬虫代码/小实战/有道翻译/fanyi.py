"""
破解有道翻译  2019年6月19日 13:27:37
主要是关键参数破解
抓包搜索后发现  salt 是一个随机数加时间戳
          sign 是 "fanyideskweb" + 翻译内容 + salt + "@6f#X3=cCuncYssPsuRUE" 用 md5加密
          bv 请求头部分用md5加密
          ts 是时间戳
"""

import requests
import time
import random
import hashlib
import json
import re

salt = str(int(time.time() * 1000)) + str(int(random.random() * 10))


class Fanyi:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.data = {
            'i': '',
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '',
            'sign': '',
            'ts': '',
            'bv': '',
            'doctype': 'json',
            'version': 'wallhaven_spider.konachan_spider',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': str(len(self.data)),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1285229729@111.79.8.190; OUTFOX_SEARCH_USER_ID_NCOO=1178262858.1156566; _ntes_nnid=888449bd7faa9c88de784ffc5f4e2c9d,1557465922780; JSESSIONID=aaaAbcXTAEt0PcHNZpUTw; ___rl__test__cookies=1560923339232',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
            'X - Requested - With': 'XMLHttpRequest',
        }
        self.salt = str(int(time.time() * 1000) + random.randint(0, 9))

    # python 自带函数实现MD5加密
    def make_md5(self, key):
        m = hashlib.md5()
        m.update(key.encode('utf-8'))
        return m.hexdigest()

    def make_sign(self, key, salt):
        sign = "fanyideskweb" + key + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        return self.make_md5(sign)

    def complete_code(self, key):
        self.data['i'] = key
        self.data['salt'] = self.salt
        self.data['sign'] = self.make_sign(key, self.salt)
        self.data['ts'] = self.salt[0:-1]
        self.data['bv'] = self.make_md5(self.headers['User-Agent'])
        # print(self.data)

    def get_data(self):
        data_str = requests.post(self.url, headers=self.headers,
                                 data=self.data).text
        print(data_str)
        data_json = json.loads(data_str)
        print(data_json)
        data_fanyi = data_json['translateResult'][0][0]['tgt']
        data_fanyi = re.sub(r'[\s]', '', data_fanyi)
        print('翻译的结果是：' + data_fanyi)
        try:
            data_chidian = data_json["smartResult"]['entries']
            print(key + ' 在词典中有以下意思：')
            for i in data_chidian[1:]:
                i = re.sub(r'[\s]', '', i)
                print(i)
        except:
            pass

    def Run(self, key):
        # konachan_spider 补全代码
        self.complete_code(key)
        # wallhaven_spider 获取数据
        data = self.get_data()


if __name__ == '__main__':
    key = input('输入翻译的内容：')
    Youdao = Fanyi()
    Youdao.Run(key)

'''
2019年7月14日 12:55:29
发现有道已经修改了代码 现在这个已经不能用了

2019年7月14日 13:20:37做了修改发现网页更新是修改了
sign = "fanyideskweb" + key + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
的最后一个参数
只要去有道的源码搜一下 sign 就能看到他每次更新换的源码是什么
'''
