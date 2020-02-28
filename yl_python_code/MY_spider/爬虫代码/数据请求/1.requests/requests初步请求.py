import requests
url = 'https://www.baidu.com/?tn=96928074_hao_pg'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
response = requests.get(url,headers = head)
data = response.content.decode("UTF-8")
print(data)
