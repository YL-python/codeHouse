import requests
import time
import random
import hashlib
import json
import re

salt = str(int(time.time() * 1000)) + str(int(random.random() * 10))


class Fanyi:
    def __init__(self, key):
        self.url = 'http://fanyi.youdao.com/' \
                   'translate_o?smartresult=dict&smartresult=rule'
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
            'version': '2.1',
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
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1285229729@111.79.8.190;'
                      ' OUTFOX_SEARCH_USER_ID_NCOO=1178262858.1156566;'
                      ' _ntes_nnid=888449bd7faa9c88de784ffc5f4e2c9d,'
                      '1557465922780; JSESSIONID=aaaAbcXTAEt0PcHNZpUTw;'
                      ' ___rl__test__cookies=1560923339232',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/74.0.3729.131 Safari/537.36',
            'X - Requested - With': 'XMLHttpRequest'
        }
        self.salt = str(int(time.time() * 1000) + random.randint(0, 9))
        self.key = key

    # python 自带函数实现MD5加密
    def make_md5(self, data):
        m = hashlib.md5()
        m.update(data.encode('utf-8'))
        return m.hexdigest()

    def make_sign(self):
        sign = "fanyideskweb" + self.key + self.salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        return self.make_md5(sign)

    def complete_code(self):
        self.data['i'] = self.key
        self.data['salt'] = self.salt
        self.data['sign'] = self.make_sign()
        self.data['ts'] = self.salt[0:-1]
        self.data['bv'] = self.make_md5(self.headers['User-Agent'])
        # print(self.data)

    def get_data(self):
        data_str = requests.post(self.url, headers=self.headers,
                                 data=self.data).text
        data_json = json.loads(data_str)
        data_fanyi = data_json['translateResult'][0][0]['tgt']
        data_fanyi = re.sub(r'[\s]', '', data_fanyi)
        return data_fanyi

    def Run(self):
        # 1 补全代码
        self.complete_code()
        # 2 获取数据
        data = self.get_data()
        print(data)
        return data


if __name__ == '__main__':
    key = input('输入翻译的内容：')
    Youdao = Fanyi(key)
    Youdao.Run()
# 发现问题超长文本会被分割 翻译
'''
过一会儿，我情不自禁地拿起水桶，兴高采烈地跑了出去，和一个大姐姐玩了起来。我们先玩起了打雪仗，
只见大姐姐以闪电般的速度拿了一大块雪，朝我用力一扔，我吓得魂飞魄散，一动不动地站在那儿，结果
当然是我被击个正着。我不甘示弱，飞快地拿起一大块雪开始反攻，以超高的命中率击中了她，我高兴得
手舞足蹈，而大姐姐呢，则气得火冒三丈，拿了三四个雪块向我猛攻，我如同一个机灵的小猴子，左躲右闪，
就这样她一个也没击中我，反而累得气喘吁吁。
'''