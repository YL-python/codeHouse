import requests
import re

url = 'http://www.netbian.com/desk/21611.htm'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

r = requests.get(url,headers = head)
r = r.content.decode('gbk')

p = re.compile('<img src="(http://img.netbian.com\S*.jpg)" alt="')
data = p.findall(r)

r = requests.get(data[0],headers = head)
#print(r.content)

with open("a.jpg","wb") as f:
    f.write(r.content)
