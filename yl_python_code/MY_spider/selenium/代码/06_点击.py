from selenium import webdriver
import time
driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
inputTag.send_keys("python")

time.sleep(5)

dianTag = driver.find_element_by_xpath('//input[@id="su"]')
dianTag.click()
