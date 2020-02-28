import requests
import os

url = 'https://pvp.qq.com/web201605/js/herolist.json'
html = requests.get(url).json()
hero_name = list(map(lambda x:x["cname"], html))
hero_id = list(map(lambda x:x["ename"], html))
index = 0
all = len(hero_name)-1
for v in hero_id:
    #创建文件夹
    os.mkdir("E:\\pycharm\\爬虫代码\\小实战\\王者官网壁纸\\tupian\\"+hero_name[index])
    #进入刚刚创建的文件夹
    os.chdir("E:\\pycharm\\爬虫代码\\小实战\\王者官网壁纸\\tupian\\"+hero_name[index])
    print("正在爬取 "+hero_name[index]+" 的性感照片      进度："+str(index)+"/"+str(all))
    index += 1
    for each in range(1,15):
        hero_url = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"+str(v)+"/"+str(v)+"-bigskin-"+str(each)+".jpg"
        data = requests.get(hero_url)
        if data.status_code == 200:
            with open(str(each)+".jpg","wb")as f:
                f.write(data.content)
        else:
            break
print("英雄们的性感照片已经全部保存到本地啦！")