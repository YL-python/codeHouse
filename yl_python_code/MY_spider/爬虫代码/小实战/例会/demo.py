#salt: 15755407052125
#sign: b90bc19963334d77c28b0bbc39498bb6
#ts: 1575540705212
#bv: 7bb9e9db2707c914156467ebfc4afb55
# salt   时间戳  + 随机整数
# sign  "fanyideskweb" + e + salt + "n%A-rKaT5fb[Gy?;N5@Tj"   进行md5加密
# ts   时间戳
# bv   请求头进行md5加密

from hashlib import md5
import time
import random
import requests
import json

word = "你好"

# md5加密函数
def my_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()

num_time = int(time.time()*1000)

num_random = int(random.random()*10)

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

data = {'i': '',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '',
        'sign': '',
        'ts': '',
        'bv': '',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'}

headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1285229729@111.79.8.190; OUTFOX_SEARCH_USER_ID_NCOO=1178262858.1156566; _ntes_nnid=888449bd7faa9c88de784ffc5f4e2c9d,1557465922780; Hm_lvt_bfc6c23974fbad0bbfed25f88a973fb0=1565444432,1565504544,1565703666; _ga=GA1.2.2113159868.1571126844; P_INFO=15170915459|1571127023|1|youdaonote|00&99|null&null&null#jix&360400#10#0|&0||15170915459; JSESSIONID=aaa6Tk_kdimSH_ISOTv7w; ___rl__test__cookies=1575540705206',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'}


data["i"] = word
data["ts"] = data["salt"][0:-1]
data["salt"] =str(int(time.time() * 1000) + random.randint(0, 9))
data["bv"] = "7bb9e9db2707c914156467ebfc4afb55"
sign = "fanyideskweb" + word + data["salt"] + "n%A-rKaT5fb[Gy?;N5@Tj"
data["sign"] = my_md5(sign)
#
# for i in data:
#     print(i + ":" + data[i])

response = requests.post(url, headers=headers,data=data).content.decode("utf-8")
print(response)
print(type(response))
print("分割线".center(50,"-"))
response_json = json.loads(response)
print(response_json)
print(type(response_json))
print("分割线".center(50,"-"))
ans =  response_json["translateResult"][0][0]["tgt"]
print(ans)
