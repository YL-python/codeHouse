import requests
import time
import random
import hashlib
import json
import re

word = "大数据"

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {
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
headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1285229729@111.79.8.190; OUTFOX_SEARCH_USER_ID_NCOO=1178262858.1156566; _ntes_nnid=888449bd7faa9c88de784ffc5f4e2c9d,1557465922780; JSESSIONID=aaaAbcXTAEt0PcHNZpUTw; ___rl__test__cookies=1560923339232',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
            'X - Requested - With': 'XMLHttpRequest',
        }

data["i"] = word
data["salt"] = str(int(time.time() * 1000) + random.randint(0, 9))
# print(data["salt"])
data['ts'] = data["salt"][0:-1]

def my_md5(key):
    m = hashlib.md5()
    m.update(key.encode('utf-8'))
    return m.hexdigest()

key = "fanyideskweb" + word + data["salt"] + "n%A-rKaT5fb[Gy?;N5@Tj"
data["sign"] = my_md5(key)
# print(data["sign"])

data['bv'] = my_md5(headers['User-Agent'])

response = requests.post(url, headers=headers,data=data).text
print(response)
print(type(response))

print("分割线".center(50,"-"))

json_response = json.loads(response)
print(json_response)
print(type(json_response))