import requests
import re
url = 'https://www.baidu.com/s?wd=计算机&pn=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

data_url = requests.get(url,headers=headers).content.decode("utf-8")
p_first = re.compile('<div class="result c-container " id="konachan_spider"(/*?)<div class="result', re.S)
data_first = p_first.findall(data_url)
print(data_first)