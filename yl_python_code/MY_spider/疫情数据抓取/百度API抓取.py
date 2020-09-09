import requests

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1'
print(url)

data = requests.get(url, timeout=10).content.decode('utf-8')
print(data)
