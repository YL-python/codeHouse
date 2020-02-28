import requests
x = input()
url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(x)
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
response = requests.get(url,headers = head)

data1 = response.content.decode("UTF-8")
data2 = response.text
#print(response.content.decode("UTF-8"))
#print(response.text)

print(response.request.url)
with open("content.txt","w") as f:
    f.write(data1)

with open("text.txt","w") as f:
    f.write(data2)

