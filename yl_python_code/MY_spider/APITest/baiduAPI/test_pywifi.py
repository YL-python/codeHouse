import pywifi
import sys
import time
from pywifi import const


def gic():
    wifi = pywifi.PyWifi()  # 创建一个无线对象
    ifaces = wifi.interifaces()[0]  # 取第一个无限网卡
    if ifaces in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        print('已连接')
    else:
        print('未连接')


gic()
