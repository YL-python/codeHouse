from selenium import webdriver
import time

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

input_Tag = driver.find_element_by_xpath('//input[@id="kw"]')
input_Tag.send_keys("python")  # 输入内容

time.sleep(3)

input_Tag.clear()   # 清空输入框