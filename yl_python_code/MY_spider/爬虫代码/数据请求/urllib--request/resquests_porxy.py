import requests
url = "https://www.baidu.com"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
        }
free_porxy = {
        "http":"27.17.45.90:43411"
}
response = requests.get(url ,headers=head,proxies=free_porxy)
print(response.status_code)
