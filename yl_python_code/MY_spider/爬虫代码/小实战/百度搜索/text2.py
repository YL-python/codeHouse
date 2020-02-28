import requests
import re
url = 'https://www.baidu.com/s?wd=计算机比赛&pn=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

data_url = requests.get(url,headers=headers).content.decode("utf-8")
p_first = re.compile('<div id="content_left">(.*?)<div style="clear:both;height:0;"></div>', re.S)
data_first = p_first.findall(data_url)
# print(data_first)


# p_xiangqing = re.compile('<em>(.*?)</div>', re.S)
# data_xiangqing = p_xiangqing.findall(str(data_first))
# # print(data_xiangqing[konachan_spider])


# 匹配标题和连接
p_2 = re.compile('<h3 class="t(.*?)</h3>', re.S)
data_2 = p_2.findall(str(data_first))

print(data_2[0])

p_3 = re.compile('>(.*?)</a>', re.S)
print(data_2[1])
for i in data_2:
    data_wenzhi = p_3.findall(i)[0].replace("<em>", '').replace("</em>", '')
    data_url = re.findall('href.?=.?"(.*?)"', i)
    print("标题:"+data_wenzhi)
    print("连接:"+data_url[0])
