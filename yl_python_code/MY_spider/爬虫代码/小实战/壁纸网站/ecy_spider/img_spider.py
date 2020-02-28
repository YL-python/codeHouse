import os
import json
import requests
from lxml import etree


url = 'https://www.ecy1.com/wp-admin/admin-ajax.php?action=zrz_load_more_posts'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
data = {'type': 'catL13',
        'paged': ''}
XpathTitle = '//h2[@class="entry-title"]/a/text()'
XpathUrl = '//h2[@class="entry-title"]/a/@href'
XpathImg = '//figure[@class="content-img-box "]/img/@src'
Save_path = 'F:\\图片\\ecy'
erroe_name = '\\/:*?"<>|'


def findFile(dirs, file):
    flag = False
    for root, dirs, files in os.walk(dirs):
        if files is None:
            continue
        else:
            if file in files:
                flag = True
                break
    return flag


def myPost(url, data):
    json_data = requests.post(url, headers=headers, data=data).text
    str_data= json.loads(json_data)
    data_x = etree.HTML(str_data["msg"])
    title_list = data_x.xpath(XpathTitle)
    url_list =data_x.xpath(XpathUrl)
    return title_list, url_list

def myGet(url):
    return requests.get(url, headers=headers).content


def save_img(img,dir):
    img_data = myGet(img)
    file_path = os.path.join(dir,img.split("/")[-1])
    try:
        with open(file_path,'wb')as f:
            f.write(img_data)
    except:
        print(img + "下载失败")


def main():
    for i in range(2,12):
        data['paged']=i
        title_list, url_list = myPost(url, data)
        for i in range(len(title_list)):
            try:
                for x in erroe_name:
                    title_list[i] = title_list[i].replace(x, " ")
                path = os.path.join(Save_path, title_list[i])
                os.makedirs(path)
            except Exception as e:
                print("创建"+path+"出问题了")
                continue
            response = myGet(url_list[i]).decode("utf-8")
            img_list = etree.HTML(response).xpath(XpathImg)
            for img in img_list:
                if findFile(Save_path,img.split("/")[-1]):
                    print("文件存在："+img)
                else:
                    print("正在下载：" + img)
                    save_img(img, path)



if __name__ == '__main__':
    main()
