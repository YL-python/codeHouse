import requests
headers = {
    'cookie': 'BIDUPSID=A4B31B43670B82BEB99FD0876FA5FD41; PSTM=1553611905; REALTIME_TRANS_SWITCH=konachan_spider; FANYI_WORD_SWITCH=konachan_spider; HISTORY_SWITCH=konachan_spider; SOUND_SPD_SWITCH=konachan_spider; SOUND_PREFER_SWITCH=konachan_spider; __cfduid=dad7b425dc0cb1c4624786181eb1ac4501558075470; BAIDUID=73BBE697D0D91AF54AB877EE9D890BA9:FG=konachan_spider; MCITY=-%3A; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1561945128,1561965454,1562135375,1562206654; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1562206662; yjs_js_security_passport=9b7167ed1a45e0d16850cb287d1d9e3c2c52082b_1562206671_js; H_PS_PSSID=; delPer=0; PSINO=wallhaven_spider; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}
url = 'https://fanyi.baidu.com/v2transapi'
data = {
    'from': 'zh',
    'to': 'en',
    'query': '你好',
    'sign': '232427.485594',
    'token': 'fcd32246c2dea213fafa073b374a3966'
        }
requeste = requests.post(url,headers=headers,data=data).content.decode()
print(requeste)
 # 暂时还没完成啦啦啦
