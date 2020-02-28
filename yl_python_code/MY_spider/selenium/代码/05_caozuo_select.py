from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')

selectTag = Select(driver.find_element_by_xpath(''))   # 找到并生成Select对象

# 操作 会点击
selectTag.select_by_index(1)
selectTag.select_by_value('')
selectTag.select_by_visible_text('')
# 取消选中
# selectTag.deselect_all()
