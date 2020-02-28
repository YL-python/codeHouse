import requests
import gevent
from gevent import monkey

monkey.patch_all()

def Download(fill_name,img_url):
    data = requests.get(url=img_url).content

    with open(fill_name,"wb")as f:
        f.write(data)

def main():
    gevent.joinall([
        gevent.spawn(Download,"i.jpg","url"),
        gevent.spawn(Download,"2.jpg","url")
        ])
    # 请求网络时会遇到延迟 gevent就可以在这个延迟的时候继续干另一个协程来提高效率

if __name__ == '__main__':
    main()