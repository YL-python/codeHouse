import re

head_post = '''
:authority: wallhaven.cc
:method: GET
:path: /search?categories=001&purity=001&topRange=1M&sorting=toplist&order=desc
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cookie: __cfduid=de79da98f23853031b031fe462a175fff1571829951; _pk_ref.1.01b8=%5B%22%22%2C%22%22%2C1577340676%2C%22https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%3A%2F%2Fwallhaven.cc%2F%22%5D; _pk_testcookie.1.01b8=1; _pk_ses.1.01b8=1; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlJZRSt6bVFnUUhMNU1HdExPVUNpWVE9PSIsInZhbHVlIjoibFhrZ2c1YUNFaGdcLzZpc0xvSFBBcGRTZStqZmwxXC9CRmZOUTRZN0Q1cm1PV2pQekZ4MHFaUElJbTM5WHltUnJQZm5tWE9lYnRqc2I0UDhPTDNSOVYxUjJzWHFtY0dJSXhSNkoxZTYzU3orbkxWR0IxU3F3dW9XUGFqNGRhNHdNTE4wb2VZQ0lBZVkzcHhzdUhrNGJpR2RLRGNCZmhqZEhPMWQ5WDRtMXFaV1o5K3A2OXFyTG5aZzNLS1hXcGxJdmoiLCJtYWMiOiI4M2JhYTgzOTZjOGFhNjhiODU2YmI4ZDMyMWU1YWMwNDgyNTk0ZDM0NmU5NzYyZjRlNmYzYjEzMTNmMTNiM2Y1In0%3D; XSRF-TOKEN=eyJpdiI6InRQWkxwWmpxSEs5aktGa0dMNnNURmc9PSIsInZhbHVlIjoiMmlWV3pRNjR6TXlDQmliS29mdW9KRnk0K2pTelwvVDlUWnhISkhoS0U1cEJjRHVrNmhwenJONGZBNE5RR25zcjYiLCJtYWMiOiI1MjQ0YTUzZTI0YTM3ZWE5N2IwZjMyYmM5NjNmOTQzNGUzMzUzYzU4NTE1NjgzYzk2M2ViNmNhODMxZDI2MzdjIn0%3D; wallhaven_session=eyJpdiI6IkF0dUduVDlodzExc0hRNzZSNUVGbGc9PSIsInZhbHVlIjoiT1NBYnhMYTBudFQyWFlOK2l0UG5pV3hOdVlhVGVQMjFjZHprWUc5c0JKWlVlWmZ2Z0VyXC9Zbk9sYjRQMlVVOW0iLCJtYWMiOiJiMmE1NTE4MDRjNjIwZTAxNGM1ZjczYzQ3YWFkZDRmY2FkOGE4OTgyZTEwMGI5MzkzYTQ0NDlkYTBmMWMzZjA0In0%3D; _pk_id.1.01b8=214a9398ccc729dc.1571829954.42.1577341889.1577340676.
referer: https://wallhaven.cc/toplist?page=2
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
'''
pattern = '^(.*?): (.*?)$'

for line in head_post.splitlines():   # \\1  \\2 是反向引用
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))