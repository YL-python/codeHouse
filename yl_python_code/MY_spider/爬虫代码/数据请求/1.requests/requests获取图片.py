import requests

response = requests.get("http://img.netbian.com/file/2019/0414/39a943addb52eba9a0579b2007570c98.jpg")

with open("a.jpg","wb") as f:
    f.write(response.content)
