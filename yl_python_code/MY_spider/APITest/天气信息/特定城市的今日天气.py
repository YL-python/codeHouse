import sys

sys.path.append('D:\\CodeHouse\\yl_python_code\\MY_spider\\APITest')

import APIconfig
import requests

# 会根据城市名称进行模糊查找
city_name = "彭泽县"

url = " {}/weather/current/{}?app_id={}&app_secret={}".format(APIconfig.HOST, city_name, APIconfig.app_id,
                                                              APIconfig.app_secret)
data = requests.get(url, timeout=10).content.decode("utf-8")

print(APIconfig.json_format(data))

"""
address： 城市具体信息，比如 “广东省 深圳市”
cityCode： 城市code
temp： 温度值
weather： 天气描述
windDirection： 风向描述
windPower： 风力描述
humidity： 湿度值
reportTime： 此次天气发布时间
"""
