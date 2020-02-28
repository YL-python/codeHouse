from selenium import webdriver
import time
import re
from lxml import etree
from selenium.webdriver.common.by import By  #寻找
from selenium.webdriver.support.ui import WebDriverWait   # 显式等待
from selenium.webdriver.support import expected_conditions as EC   # 等待条件

class LagouSpider():
    driver_path = r'E:\ChromeDriver\chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_%E5%8C%97%E4%BA%AC?labelWords=&fromSearch=true&suginput='
        self.cnt = 0
    def Run(self):
        max_ye = True
        self.driver.get(self.url)

        while max_ye:
            source = self.driver.page_source
            try:
                next_pageTag = WebDriverWait(self.driver, 10).until(  # 等待10秒直到
                    lambda b : b.find_element_by_xpath(('//span[@class="pager_next "]'))
                )
            except:
                max_ye = False
            self.Get_zhiye_url(source)
            next_pageTag = self.driver.find_element_by_xpath('//span[@class="pager_next "]')
            next_pageTag.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(2)

        print('全部爬完了。。。')
        print("爬虫出错了" + str(self.cnt) + " 次")

    def Get_zhiye_url(self,data):
        time.sleep(1)
        list_page = []
        soure = etree.HTML(data)
        list_a_page = soure.xpath('//div[@class="p_top"]/a/@href')
        for i in list_a_page:
            list_page.append(i)
        for page in list_page:
            print("*" * 100)
            try:
                self.driver.execute_script("window.open('{}')".format(page))
                self.driver.switch_to.window(self.driver.window_handles[1])
                print(self.driver.current_url+str(list_a_page.index(page)))
                WebDriverWait(self.driver, 10).until(
                    lambda b: b.find_element_by_xpath('//em[@class="fl-cn"]')
                )
                self.Get_data(self.driver.page_source)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
            except:
                self.cnt += 1
                print('爬虫出错了' + str(self.cnt) + " 次。。。")


    def Get_data(self,data):
        time.sleep(1)
        data_dist = {}
        data = etree.HTML(data)
        gongshi_name = data.xpath('//em[@class="fl-cn"]/text()')[0].strip()
        data_dist['公司'] = gongshi_name
        zhiwei = data.xpath('//div[@class="job-name"]/@title')[0].strip()
        data_dist['招聘职位'] = zhiwei
        gongzhi = data.xpath('//dd[@class="job_request"]/p/span[@class="salary"]/text()')[0].strip()
        data_dist['工资'] = gongzhi
        didian = data.xpath('//dd[@class="job_request"]/p/span[wallhaven_spider]/text()')[0].strip()
        didian = re.sub(r"[\s/]",'',didian)
        data_dist['地点'] = didian
        jingyan = data.xpath('//dd[@class="job_request"]/p/span[3]/text()')[0].strip()
        jingyan = re.sub(r"[\s/]", '', jingyan)
        data_dist['经验'] = jingyan
        xueli = data.xpath('//dd[@class="job_request"]/p/span[4]/text()')[0].strip()
        xueli = re.sub(r"[\s/]", '', xueli)
        data_dist['学历'] = xueli
        quanzhi = data.xpath('//dd[@class="job_request"]/p/span[5]/text()')[0].strip()
        quanzhi = re.sub(r"[\s/]", '', quanzhi)
        data_dist[r'全or兼职'] = quanzhi
        youhuo = data.xpath('//dd[@class="job-advantage"]/p/text()')[0].strip()
        data_dist['职位诱惑'] = youhuo
        # miaoshu = data.xpath('//div[@class="job-detail"]//text()')
        # miaoshu = ''.join(miaoshu)
        # miaoshu  = re.sub(r"[\s]", '', miaoshu)
        # data_dist['描述'] = miaoshu
        didian_list = data.xpath('.//div[@class="work_addr"]//text()')
        l = len(didian_list)-2
        didian = ''
        for i in range(0,l):
            didian_list[i].strip()
            didian = didian + didian_list[i]
        didian = re.sub(r"[\s]", '', didian)
        data_dist['地点'] = didian
        print(data_dist)
        self.Save_data(data_dist)

    def Save_data(self,data):
        pass

if __name__ == '__main__':
    spider = LagouSpider()
    spider.Run()

"""
起始页 解析源代码获取15职位信息链接
for 打开链接 转页面 获取源代码 解析
保存 
翻页 解析源代码获取15职位信息链接
for 打开链接 转页面 获取源代码 解析
保存
翻页
。。。。

最后一页保存之后退出程序

注意 用到AJAX的页面要用到显式等待
"""
