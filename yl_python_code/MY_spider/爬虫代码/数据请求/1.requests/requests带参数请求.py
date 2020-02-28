import requests
url = 'https://www.baidu.com/s'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
kw = {'wd':'美女'}
response = requests.get(url,headers = head,params = kw)
data = response.content.decode("UTF-8")
print(data)

