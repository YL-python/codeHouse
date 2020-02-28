"""
2019年8月24日10点33分
numpy 数值修改

python的三元运算符   a = 3 if 4>3 else 4

布尔索引
numpy 的三元运算符 where
裁剪函数  clip()

a = b   b的值会有ab同时影响
a = b.copy()  a b 互不影响
"""

import numpy as np

# 把数组数值小于10的全部变成3
# 布尔索引  修改True索引的值
t1 = np.arange(24).reshape((4, 6))
print(t1)
print(t1 < 10)  # <10 的为True
t1[t1 < 10] = 3  # 把索引是True的全部变成3
print(t1)

print('*' * 20)

# 把小于10的变成0  大于10的变成10
t2 = np.arange(24).reshape((4, 6))
# numpy 的三元运算符  where
t2 = np.where(t2 < 10, 0, 10)  # 有返回值
# t2 = np.where(t2 < 10, t2-10, t2+10)  # 有返回值
print(t2)
print('*'*20)

t3 = np.arange(24, dtype='float').reshape((4, 6))
t3[t3 > 20] = np.nan
print(t3)
# 把小于10的变成10   大于18的变成18
t3 = t3.clip(10, 18)   # 源码的意思就是小于10的全部变成10   大于18的全部变成18
print(t3)   # 发现 nan 这个值没有被改变
