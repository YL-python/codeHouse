import requests
from bs4 import BeautifulSoup

url = 'https://www.chainnode.com'
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}

url_str = requests.get(url,headers = head).content.decode("utf-8")

#转解析类型
soup = BeautifulSoup(url_str,'lxml')

#result = soup.select('h3 a,.link-dark-major font-bold bbt-block')
#for i in result:
#    print(i.get_text())

result = soup.select('h3 a')
for i in result:
    print(i.get_text())
'''
for i in result:
    print(i.get('href'))
    i=i.string.replace(' ','')
    print(i)
    print(i.get('href'))
'''
