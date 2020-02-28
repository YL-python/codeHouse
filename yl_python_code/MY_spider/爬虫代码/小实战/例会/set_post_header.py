import re

head_post = '''
i: request
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15755407052125
sign: b90bc19963334d77c28b0bbc39498bb6
ts: 1575540705212
bv: 7bb9e9db2707c914156467ebfc4afb55
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
'''
pattern = '^(.*?): (.*?)$'

for line in head_post.splitlines():   # \\konachan_spider \\wallhaven_spider 是反向引用
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))