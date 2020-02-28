from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait   # 显式等待
from lxml import etree
import os
import requests
import re
import time


class Wz_spider():
    driver_path = r'E:\ChromeDriver\chromedriver.exe'
    def __init__(self):
        # self.option = webdriver.ChromeOptions()
        # self.option.add_argument('headless')     options=self.option
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://pvp.qq.com/web201605/wallpaper.shtml'
        self.head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}
        self.x = True


    def Get_bz_url_list(self,data):
        data = etree.HTML(data)
        bizhi_name_list2 = []
        bizhi_name_list1 = data.xpath('//div[@id="Work_List_Container_267733"]/div/img/@alt')
        bizhi_url_list = data.xpath('//div[@id="Work_List_Container_267733"]/div/ul/li[5]/a/@href')
        print(bizhi_name_list1)
        for name in bizhi_name_list1:
            name = re.sub(r"[\/?:*<>|]", 'X', name)
            bizhi_name_list2.append(name)
        self.Save_data(bizhi_url_list,bizhi_name_list2)

    def Save_data(self,url_list,name_list):
        os.chdir(r'E:\pycharm\爬虫代码\小实战\se实现爬王者壁纸\Tupian')
        index = 0
        for url in url_list:
            # print(name_list[index])
            data = requests.get(url,headers = self.head).content
            with open(name_list[index]+str(index)+'-.png','wb')as f:
                f.write(data)
            index += 1

    def Run(self):
        # 打开网页
        self.driver.get(self.url)
        while self.x:
            time.sleep(3)
            try:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                WebDriverWait(self.driver,10).until(
                    lambda d: d.find_element_by_xpath('//div[@id="Work_List_Container_267733"]/div[@class="p_newhero_item"]')
                )
                source = self.driver.page_source
                # 分析出当前页的壁纸链接和 名字
                self.Get_bz_url_list(source)
                # 保存
                # 翻页
                nextTag = WebDriverWait(self.driver,10).until(
                    lambda d: d.find_element_by_xpath('//div[@class="pagingPanel"]/a[@class="downpage"]')
                )
                nextTag.click()
            except:
                self.x = False
        try:
            source = self.driver.page_source
            bizhi_url_list, bizhi_name_list = self.Get_bz_url_list(source)
            self.Save_data(bizhi_url_list, bizhi_name_list)
        except:
            print("爬完啦！")

if __name__ == '__main__':
    wz = Wz_spider()
    wz.Run()