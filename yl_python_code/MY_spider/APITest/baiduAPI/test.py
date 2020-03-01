import requests
import time

url = "https://api.map.baidu.com/locapi/v2"

header = {
    "key": "xLbL8WZK0RmwA98VThCPB0xSRSS27ulK",
    "src": "aaa",
    "prod": "aaa",
    "ver": "1.0",
    "trace": "0"
}
data = {
    "accesstype": 1,
    "macs": 1,
    "ctime": str(int(time.time()*1000)),
}
response = requests.post(url, data=data, headers=header).content.decode("utf-8")
print(response)
