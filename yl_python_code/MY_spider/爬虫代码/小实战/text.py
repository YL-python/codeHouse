import re
import time
import requests
#定义url
get_url = "http://www.ireadweek.com/index.php?g=portal&m=index&a=index&p=1"
#定义头部
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.konachan_spider; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
response = requests.get(url=get_url,headers=headers)
ret = response.text
#print(ret)

#爬取的内容
#书籍
read = re.findall('<div class="hanghang-list-name">(.*?)</div>',ret,re.S)
#豆瓣评分
score = re.findall('<div class="hanghang-list-num">(.*?)</div>',ret,re.S)
#作者
aut = re.findall('<div class="hanghang-list-zuozhe">(.*?)</div>',ret,re.S)
# print(read)
# print(len(read))
# print(score)
# print(len(score))
# print(aut)
# print(len(aut))
# for read_i, score_i, aut_i in zip(read,score,aut):
#    print(read_i, score_i,aut_i)
# for i in range(len(read)):
# #     print(i,end=',')
a = [0,1,2]
print(a[0],a[1],a[2])
for i in range(len(a)):
    print(a[i])