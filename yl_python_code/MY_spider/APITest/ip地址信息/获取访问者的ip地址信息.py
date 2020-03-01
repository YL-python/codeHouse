import sys

sys.path.append('D:\\CodeHouse\\yl_python_code\\MY_spider\\APITest')

import APIconfig
import requests

url = "{}/ip/self?app_id={}&app_secret={}".format(APIconfig.HOST, APIconfig.app_id, APIconfig.app_secret)
data = requests.get(url, timeout=10).content.decode("utf-8")

print(APIconfig.json_format(data))
"""
ip： 访问者的ip地址
province： 省份
provinceId： 省份id
city： 城市
cityId： 城市id
isp： 网络服务商名称 例如 电信
desc： 拼接好的描述信息
"""