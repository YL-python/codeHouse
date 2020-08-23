import requests
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
url = ['http://test.isiyuan.net/tiangou/tg.php', 'https://api.ixiaowai.cn/tgrj/index.php']

try:
    allData = json.load(open("舔狗日记2.json", "r", encoding='utf-8'))
except:
    allData = []
print("开始数据长度 {}".format(len(allData)))

for i in range(100):
    data = requests.get(url[1], headers=HEADERS).content.decode('utf-8').replace('2020年08月17日Mon 晴 ', '')
    print("正在请求第 {} 条数据  ".format(i) + data)
    allData.append(data)

allData = list(set(allData))
print("结束数据长度 {}".format(len(allData)))

json.dump(allData, open("舔狗日记2.json", "w", encoding='utf-8'), ensure_ascii=False)
