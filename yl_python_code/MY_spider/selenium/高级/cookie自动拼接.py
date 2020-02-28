str = 'UM_distinctid=16ab5e35b6f54e-00adbd99217da4-70193c4f-e1000-16ab5e35b701e2; ccid=d7875cf523b2cb0948e3e403f5218141; csrftoken=37411479b6799969fe9eacb72b76d243; tt_webid=6690827985601709571; odin_tt=475fec1098ed99b8392a79a40701398d45d11d2fc6d0a35ed71fb41bc9ada59ca6cdd7c474d8c9ea63af20774fb998a6eb535e97ce9caebc586470e9001356b9; passport_auth_status=71959c0ce2298ada318f05142d0bb7f5; sso_uid_tt=4fe42273ba171bddfeb284ec9ca4317d; toutiao_sso_user=f818f9f9deddc0c5ae00e6a438e5183a; sessionid=c921e8edde024c89005aa64a9d6de067; uid_tt=95fc0031f8a9aa94070545cf4f27972be3fde88393b1b4a88216b04e8ea66596; __tea_sdk__ssid=undefined; tt_webid=6690827985601709571; WEATHER_CITY=%E5%8C%97%E4%BA%AC; CNZZDATA1259612802=1986326866-1557829729-%7C1557829729; __tasessionId=hb3sdlogq1557830348749'

str = str.replace('"','')

str_list = str.split(';')

cookie_list = []

for item in str_list:
      name_value = {}
      name_value['name'] = item.split('=')[0].strip()
      name_value['value'] = item.split('=')[1]
      cookie_list.append(name_value)

print(cookie_list)

