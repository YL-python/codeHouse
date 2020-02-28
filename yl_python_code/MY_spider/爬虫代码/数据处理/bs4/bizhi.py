from bs4 import BeautifulSoup
import requests
url = 'http://www.netbian.com/desk/21828.htm'

data_url=requests.get(url).content.decode('gbk')

soup = BeautifulSoup(data_url,"lxml")

result = soup.select('div p a img')[0].get('src')
print(result)

