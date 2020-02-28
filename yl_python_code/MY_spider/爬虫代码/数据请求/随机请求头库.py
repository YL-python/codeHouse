from fake_useragent import UserAgent
ua = UserAgent()
headers1= {
    "User-Agent" : ua.random
}
headers2= {
    "User-Agent" : ua.random
}
headers3= {
    "User-Agent" : ua.random
}
print(headers1)
print(headers2)
print(headers3)
