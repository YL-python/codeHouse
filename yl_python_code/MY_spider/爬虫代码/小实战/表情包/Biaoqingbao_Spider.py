import requests
from lxml import etree
import os
import re

class Biaoqingbao_Spider(object):
    def __init__(self):
        self.url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
        self.url_list = list()
        self.url_error = 'https://fabiaoqing.com'

    def Pingjie_url(self,num1,num2):
        for i in range(num1,num2):
            self.url_list.append(self.url.format(i))

    def Get_data(self,url):
        data = requests.get(url = url, headers = self.headers).content
        return data

    def Xpath_data(self,data):
        data = etree.HTML(data)
        data_url_list = data.xpath('//div[@id="bqb"]/div/div/a/img/@data-original')
        data_name_list = data.xpath('//div[@id="bqb"]/div/div/a/@title')
        return data_url_list, data_name_list

    def Save_data(self,data_list,data_name):
        try:
            os.mkdir('../表情包/下载')
        except:
            pass
        index = 0
        try:
            os.chdir('../表情包/下载')
        except:
            pass
        for url in data_list:
            try:
                data = self.Get_data(url)
            except:
                url = self.url_error + url
                data = self.Get_data(url)
            file_name = str(data_name[index]) + str(url[-4:])
            file_name = re.sub(r'[<>/\\|:"\\*\\?\s]', '', file_name)

            if os.path.exists(file_name):
                pass
                # print('\r{}已存在'.format(file_name),end='')
            else:
                try:
                    # print('正在下载：'+file_name)
                    with open(file_name,'wb')as f:
                        f.write(data)
                except:
                    pass
            index += 1


    def Run(self,num1, num2):
        # konachan_spider、拼接地址
        print(num1, num2)
        self.Pingjie_url(num1,num2)
        for url in self.url_list:
            # wallhaven_spider、发送请求
            data = self.Get_data(url).decode('utf-8')
            # 3、解析数据
            data_url_list, data_name_list = self.Xpath_data(data)
            # 4、保存
            self.Save_data(data_url_list,data_name_list)


if __name__ =="__main__":
    Bqb_Spider = Biaoqingbao_Spider()
    import threading
    t1 = threading.Thread(target=Biaoqingbao_Spider.Run,args=(Bqb_Spider,1,20*1))
    t2 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*1, 20*2))
    t3 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*2, 20*3))
    t4 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*3, 20*4))
    t5 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*4, 20*5))
    t6 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*5, 20*6))
    t7 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*6, 20*7))
    t8 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*7, 20*8))
    t9 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*8, 20*9))
    t10 = threading.Thread(target=Biaoqingbao_Spider.Run, args=(Bqb_Spider, 20*9, 20*10))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    # Bqb_Spider.Run()