import requests


url = "https://s1.maomibf1.com/common/nvyou/20191128/sMnktqBu/sMnktqBu{}.ts"

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}

for i in range(30, 586):
    print(i)
    data = requests.get(url.format(i), headers=header).content
    with open("aaa\\{}".format(i), "ab")as f1:
        f1.write(data)