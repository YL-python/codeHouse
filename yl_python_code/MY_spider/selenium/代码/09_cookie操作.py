from selenium import webdriver

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.hao123.com/")

for cookie in driver.get_cookies():
    print(cookie)

print('#'*40) #用值去找
print(driver.get_cookie('tnwhiteft'))

print('#'*40) #删除cookie
print(driver.delete_cookie('tnwhiteft'))

#删除所有cookie
driver.delete_all_cookies()
