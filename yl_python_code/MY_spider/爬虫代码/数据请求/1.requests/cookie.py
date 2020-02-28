import requests

session = requests.session()

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
url = 'http://www.renren.com/PLogin.do'
post_data = {
    "email":"15170915459","password":"5952768yl"
    }
session.post(url,data=post_data,headers=head)
r = session.get("http://www.renren.com/970526101/profile",headers = head)
print(r.content)
