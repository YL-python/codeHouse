# 测试点击a标签

from selenium import webdriver
import time
driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=sug&suginput=Python")

time.sleep(2)

dianTag = driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
dianTag.click()
print(driver.current_url)
time.sleep(2)
dianTag = driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
dianTag.click()
print(driver.current_url)
time.sleep(2)
dianTag = driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
dianTag.click()
print(driver.current_url)
time.sleep(2)