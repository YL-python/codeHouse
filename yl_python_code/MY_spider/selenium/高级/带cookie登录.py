from selenium import webdriver

driver_path = r'E:\ChromeDriver\chromedriver.exe'
option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome(executable_path=driver_path, options=option)

# cookie要先解析成 name value的形式

cookie_toutiao = [{'name': 'UM_distinctid', 'value': '16ab5e35b6f54e-00adbd99217da4-70193c4f-e1000-16ab5e35b701e2'}, {'name': 'ccid', 'value': 'd7875cf523b2cb0948e3e403f5218141'}, {'name': 'csrftoken', 'value': '37411479b6799969fe9eacb72b76d243'}, {'name': 'tt_webid', 'value': '6690827985601709571'}, {'name': 'odin_tt', 'value': '475fec1098ed99b8392a79a40701398d45d11d2fc6d0a35ed71fb41bc9ada59ca6cdd7c474d8c9ea63af20774fb998a6eb535e97ce9caebc586470e9001356b9'}, {'name': 'passport_auth_status', 'value': '71959c0ce2298ada318f05142d0bb7f5'}, {'name': 'sso_uid_tt', 'value': '4fe42273ba171bddfeb284ec9ca4317d'}, {'name': 'toutiao_sso_user', 'value': 'f818f9f9deddc0c5ae00e6a438e5183a'}, {'name': 'sessionid', 'value': 'c921e8edde024c89005aa64a9d6de067'}, {'name': 'uid_tt', 'value': '95fc0031f8a9aa94070545cf4f27972be3fde88393b1b4a88216b04e8ea66596'}, {'name': '__tea_sdk__ssid', 'value': 'undefined'}, {'name': 'tt_webid', 'value': '6690827985601709571'}, {'name': 'WEATHER_CITY', 'value': '%E5%8C%97%E4%BA%AC'}, {'name': 'CNZZDATA1259612802', 'value': '1986326866-1557829729-%7C1557829729'}, {'name': '__tasessionId', 'value': 'hb3sdlogq1557830348749'}]

driver.get('https://www.toutiao.com/')
for cookie in cookie_toutiao:
    driver.add_cookie(cookie)

driver.get('https://www.toutiao.com/')
print(driver.title)