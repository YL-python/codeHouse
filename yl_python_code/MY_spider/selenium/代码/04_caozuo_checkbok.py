from selenium import webdriver
import time

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')

rememberTag = driver.find_element_by_xpath('//p[@class="account-form-remember"]/input')  # 多种方法选中
rememberTag.click()

time.sleep(3)

rememberTag.click()