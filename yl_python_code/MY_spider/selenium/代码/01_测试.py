# encoding = 'gbk'
# 导入模块
from selenium import webdriver
import time

# 指定路径  r 表示纯字符串 忽略 \ / 等的转义
driver_path = r'E:\ChromeDriver\chromedriver.exe'
# 创建一个Chrome的对象
driver = webdriver.Chrome(executable_path=driver_path)
# 打开指定网页
driver.get('https://www.baidu.com/')
# 打印网页源代码
# print(driver.page_source)

time.sleep(5)

#driver.close()
driver.quit()