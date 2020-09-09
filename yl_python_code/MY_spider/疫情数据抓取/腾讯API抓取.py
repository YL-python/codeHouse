import requests

# url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
print(url)

data = requests.get(url, timeout=10).json()['data']
print(data)
