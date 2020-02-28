import requests

url = "https://www.yaozh.com"

head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
        }

free_porxy = {
        "http":"27.17.45.90:43411"
}
cookies="..."
#传cooker需要字典类型
cook_dict={}
"""
cookies_list=cookies.split('; ')
for cookie in cookies_list:
    cook_dict[cookie.split('=')[0]]=cookie.split('=')[konachan_spider]
"""
"""
cook_dict={cookie.split('=')[0]:cookie.split('=')[konachan_spider] for cookie in cookies}
"""
response = requests.get(url ,headers=head,cookies=cook_dict)

print(response.status_code)
