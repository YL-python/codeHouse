# encoding = 'utf-8'
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element(By.ID,'kw')

# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element(By.NAME,'wd')

# inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag = driver.find_element(By.CLASS_NAME,'s_ipt')

# inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
inputTag = driver.find_element(By.XPATH,'//input[@id="kw"]')

# 注意注意 By.XPATH 方法只能找到元素找不到元素的text() 属性

inputTag.send_keys('python')

# 获取数据的时候应该
# from lxml import etree
# html = etree.HTML(driver.page_source)
# html.xpath("")
#因为lxml是用c 语言编写 运行速度会快一些