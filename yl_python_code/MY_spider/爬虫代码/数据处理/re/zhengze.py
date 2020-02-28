import urllib.request
import re

url = 'https://movie.douban.com/top250'
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}

request = urllib.request.Request(url,headers=head)
response = urllib.request.urlopen(request).read().decode("UTF-8")

#print(response)
result = re.findall("<span class=\"title\">([\u4e00-\u9fa5]+)",response)
for i in result:
    print(i)
