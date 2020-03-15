import sys

sys.path.append('D:\\CodeHouse\\yl_python_code\\MY_spider\\APITest')

import APIconfig
import requests

# 会根据城市名称进行模糊查找
city_name = "彭泽县"

url = " {}/weather/forecast/{}?app_id={}&app_secret={}".format(APIconfig.HOST, city_name, APIconfig.app_id, APIconfig.app_secret)
print(url)

data = requests.get(url, timeout=10).content.decode("utf-8")

print(APIconfig.json_format(data))
"""
address： 城市具体信息，比如 “广东省 深圳市”
cityCode： 城市code
reportTime： 此次天气发布时间
forecasts： 今天及未来天气列表
    date： 日期
    dayOfWeek： 星期
    dayWeather： 白天天气描述
    nightWeather： 晚上天气描述
    dayTemp： 白天温度
    nightTemp： 晚上温度
    dayWindDirection： 白天风向
    nightWindDirection： 晚上风向
    dayWindPower： 白天风力
    nightWindPower： 晚上风力

"""