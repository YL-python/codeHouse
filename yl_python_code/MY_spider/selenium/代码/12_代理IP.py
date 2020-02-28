from selenium import webdriver

driver_path = r'E:\ChromeDriver\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http//112.87.68.63:9999")

driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get('http://www.httpbin.org/ip')