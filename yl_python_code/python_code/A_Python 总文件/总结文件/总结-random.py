# -*- coding: UTF-8 -*-

import random

# 随机整数：
print(random.randint(1,50))

# 随机选取0到100间的偶数：
print(random.randrange(0, 101, 2))

# 随机浮点数：
print(random.random())   # [0,1)  之间的浮点数
print(random.uniform(1, 10))   #[1,10)  之间的浮点数

# 可迭代序列中随机选择：
print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))

# 从可迭代对象中生成指定数量的随机字符：  返回结果是列表
print(random.sample('zyxwvutsrqponmlkjihgfedcba',5))

# 多个字符中选取指定数量的字符组成新字符串：
print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))

# 随机选取字符串：
print(random.choice(['剪刀', '石头', '布']))

# 打乱 可迭代对象
lists = [1,2,3,4,5]
random.shuffle(lists)
print(lists)