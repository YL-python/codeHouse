import requests

url = "https://www.yaozh.com/login/"
session = requests.session()#自动保存cookies
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
        }
login_from_data = {
    'username':'15170915459',
    'pwd':'5952768yl',
    'formhash':'8095494CAA',
    'backurl':'https%3A%2F%2Fwww.yaozh.com%2F'
    }

response = session.post(url ,data=login_from_data,headers=head)
#先登录 登录成功后带着有效的cookies去请求目标数据
#session会自动保存cookie

member_url="https://www.yaozh.com/member/"
data=session.get(member_url , headers=head).content
with open('diyi.html','wb') as f:
    f.write(data)
