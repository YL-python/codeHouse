import requests
from lxml import etree
import analysis_json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/74.0.3729.131 Safari/537.36'}
url = analysis_json.get("江西省","南昌")[0]
print(url)
response = requests.get(url,headers).content.decode("utf-8")
Xpath_data = etree.HTML(response)

time3_data = []
for i in range(1,9):
    if i == 2:
        day = list()
        day.append("气温")
        day1 = Xpath_data.xpath('//div[@id="day0"]/div[2]/div/img/@src')
        for i in range(len(day1)):
            day1[i] = re.sub(r"[\s]", '', day1[i])
            day.append(day1[i])
        time3_data.append(day)

    day = Xpath_data.xpath('//div[@id="day0"]/div[{}]/div/text()'.format(i))
    for i in range(len(day)):
        day[i] = re.sub(r"[\s]", '', day[i])
    time3_data.append(day)
print(time3_data)

day7_data = []
def xpath_data(miaoshu,num,s):
    data = [miaoshu]
    for i in range(1, 8):
        day = Xpath_data.xpath(
            '//div[@class="detail"][{}]/div/table/tbody/tr[{}]/td/text()'.format(i,num))
        if len(day) == 2:
            if day[0] == day[1]:
                day = day[0]
            else:
                day = day[0] + s + day[1]
                day = day.replace(" ", '')
        else:
            day = day[0]
        data.append(day)
    day7_data.append(data)

data_riqi = ["日期"]
for i in range(1,4):
    day = Xpath_data.xpath(
        '//div[@class="detail"][{}]/div/table/tbody/tr[1]/td[2]/text()'.format(i))[0]
    day = re.sub(r"[\s]", '', day)
    data_riqi.append(day)

for i in range(4,8):
    day = Xpath_data.xpath(
        '//div[@class="detail"][{}]/div/table/tbody/tr[1]/td[1]/text()'.format(
            i))[0]
    day = re.sub(r"[\s]", '', day)
    data_riqi.append(day)
day7_data.append(data_riqi)

data_img = ["图片"]
for i in range(1,8):
    day = Xpath_data.xpath(
        '//div[@class="detail"][{}]/div/table/tbody/tr[2]/td/img/@src'.format(
            i))[0]
    day = re.sub(r"[\s]", '', day)
    data_img.append(day)
day7_data.append(data_img)

data_img = ["图片"]
for i in range(1,8):
    day = Xpath_data.xpath(
        '//div[@class="detail"][{}]/div/table/tbody/tr[2]/td/img/@src'.format(
            i))[0]
    day = re.sub(r"[\s]", '', day)
    data_img.append(day)
day7_data.append(data_img)

xpath_data("天气",3, "转")
xpath_data("温度",4, "至")
xpath_data("风向",5, "转")
xpath_data("风力",6, "转")



print(day7_data)