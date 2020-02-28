import requests

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
url = "http://www.baidu.com/"
proxies = {'HTTPS': 'HTTPS\\119.101.113.141:9999'}

r = requests.get(url,proxies= proxies,headers = head)
print(r.status_code)