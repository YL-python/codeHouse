from selenium import webdriver

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

driver.execute_script("window.open('https://www.douban.com/')")  # 打开新的窗口

print(driver.current_url)   # 打印driver的URL

print(driver.window_handles) # 获得窗口句柄

driver.switch_to.window(driver.window_handles[1])   # 切换窗口
print(driver.current_url)