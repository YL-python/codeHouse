import requests
import re
import requests
class Music_spider():
    def __init__(self):
        self.url = 'http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery172048545188079073176_1557142029285&songid={}&from=web&_=1557142031640'

    def Get_url(self,num):
        data = requests.get(self.url.format(num)).content
        return data

    def Print_data(self,data):
        print(data)
        music_name = re.compile(r'"title":"(.*?)"')
        music_url = re.compile(r'"file_link":"(.*?)"')
        music_art = re.compile(r'"artist_name":"(.*?)"')
        art_name = music_art.findall(data)[0].replace('\\', '')
        url_music = music_url.findall(data)[0].replace('\\', '')
        music_title = music_name.findall(data)[0].replace('\\', '')
        print(music_title+":"+art_name)
        print("歌曲下载链接："+url_music)

    def Run(self):
        print("请在千千音乐内找到歌曲ID并输入：")
        num_id = eval(input())
        data_html = self.Get_url(num_id).decode('utf-8')
        self.Print_data(data_html)

if __name__ == "__main__":
    Music_spider().Run()