# 基于ajax技术 很多网页是先打开网页在来慢慢加载元素   我们selenium是打开一个网页后立刻去寻找元素
# 就可能我们的元素是ajax加载的 我们立即去获取获取不到要等待他加载出来了才能获取的到
# 说以我们弄一个等待 有两种 一个是隐式等待 指定一个时间 就等那么长时间之后再继续操作
# 还有一个显式等待 指定一个时间 指定时间内我们要的元素加载出来了就不等待了直接操作 若没加载出来会抛出异常
from selenium import webdriver
from selenium.webdriver.common.by import By  #寻找
from selenium.webdriver.support.ui import WebDriverWait   # 显式等待
from selenium.webdriver.support import expected_conditions as EC   # 等待条件

driver_path = r'E:\ChromeDriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.hao123.com/')

# driver.implicitly_wait(10)   # 隐式等待10秒 先找这个id 找不到会等待10秒再找
# driver.find_element_by_id('1232412')

WebDriverWait(driver,10).until(   # 等待10秒直到
    EC.presence_of_all_elements_located((By.NAME ,'word'))  # 找到这个元素
    #By.XPATh 方法只能找到元素 找不到元素的Text()属性
)
# inputTag.get_attribute()
# 元素是 webdriver对象 要获取属性或者文本用 .get_attribute('属性') 方法
