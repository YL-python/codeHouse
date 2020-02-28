import requests
url = 'https://www.baidu.com/?tn=96928074_hao_pg'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
response = requests.get(url,headers = head)

request_headers = response.request.headers
print("获取请求头：%s "%request_headers)
print(end = '\n')
response_headers = response.headers
print("获取响应头：%s "%response_headers)
print(end = '\n')
request_code = response.status_code
print("获取状态码：%s "%request_code)
print(end = '\n')
'''
request_cookie = response.repuest.cookies
print("获取请求cookie：%s "%request_cookie)
print(end = '\n')
'''
response_cookie = response.cookies
print("获取响应的cookie：%s "%response_cookie)
print(end = '\n')
request_url = response.request.url
print("获取请求的URL：%s "%request_url)
print(end = '\n')
response_url = response.url
print("获取响应的URL：%s "%response_url)
print(end = '\n')
