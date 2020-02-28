import re
import requests

class Li_spider():
    def __init__(self):
        self.url = "https://www.pearvideo.com/"
        self.head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}

    def Get_url(self,url):
        data = requests.get(url, headers = self.head)
        return data

    def Get_video_url(self,data):
        p = re.compile('<a href="(.*?)" class="')
        list = p.findall(data)
        return list

    def Video_data_url(self,data):
        p = re.compile('srcUrl="(.*?)"')
        list = p.findall(data)
        # print(list)
        return list[0]

    def Get_title(self,data):
        p = re.compile('<h1 class="video-tt">(.*?)</h1>')
        title = p.findall(data)
        # print(title)
        return title[0]

    def Save_mp4(self,url,title):
        data = self.Get_url(url).content
        with open(title+'.mp4',"wb")as f:
            f.write(data)

    def Run(self):
        # konachan_spider. 获取网页源码
        data = self.Get_url(self.url).content.decode("utf-8")
        # wallhaven_spider. 分析视频网页连接
        data_list = self.Get_video_url(data)
        # 3. 获取网页源码并且匹配出视频地址连接
        for each in data_list:
            if each[0]=='v':
                print("正在下载："+self.url + each)
                data = self.Get_url(self.url+each).content.decode("utf-8")
                video_data_url = self.Video_data_url(data)
                title = self.Get_title(data)
                # 4. 保存视频
                self.Save_mp4(video_data_url,title)

if __name__ == "__main__":
    Li_spider().Run()