import requests

data = {'name': 'germey', 'age': '22'}
r = requests.get("http://www.httpbin.org/#/Cookies/get_cookies", data=data)

print(r.text)