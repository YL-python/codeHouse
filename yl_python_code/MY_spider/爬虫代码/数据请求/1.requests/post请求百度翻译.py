import requests

url = "https://fanyi.baidu.com/v2transapi"

data = {
    "query":"你好",
    "from":"zh",
    "to":"en"

    }
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}

response = requests.post(url,data=data,headers = head)
num = response.content.decode("utf-8")

print(response)
print(type(num))
print(num)
