# 行为链多用在测试上 爬虫用的少

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'E:\ChromeDriver\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.hao123.com/')

inputTag = driver.find_element_by_xpath('//input[@data-hook="searchInput"]')
dianTag = driver.find_element_by_xpath('//input[@data-hook="searchSubmit"]')

# 构建行为链对象
action = ActionChains(driver)
#写要做的事件
action.move_to_element(inputTag)# 鼠标移动到inputTag
action.send_keys_to_element(inputTag,'python')# 向inputTag输入内容
action.move_to_element(dianTag)# 鼠标移动到点击按钮上
action.click(dianTag)# 点击 点按钮

action.perform() #执行事件