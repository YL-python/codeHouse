from selenium import webdriver

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

driver.execute_script("window.open('https://www.douban.com/')")  # ���µĴ���

print(driver.current_url)   # ��ӡdriver��URL

print(driver.window_handles) # ��ô��ھ��

driver.switch_to.window(driver.window_handles[1])   # �л�����
print(driver.current_url)