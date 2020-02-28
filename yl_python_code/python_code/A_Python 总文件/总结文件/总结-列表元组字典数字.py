# 1 列表元素
list1=[0,1,2,3,4]
# 0索引 012345  或者-n.....-3 -2 -1
# 1切片  开始：结束：步长
# 2元素个数  len()
# 3列表末尾添加元素   list.append()
# 4计算某元素在列表中的个数   list.count()
# 5删除元素 默认最后一个 返回移除的值 list.pop(index=-1)
# 6查找元素位置   list.index()
# 7列表元素反向   list.reverse()
# 8排序   list.sort()

# 2 元组
print(type( (50) ))
print(type( (50,) ))   # 注意这个就可以了

# 元组转列表  list()
# 列表转元组  tuple()

# 3 字典
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对  之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
# d = {key1 : value1, key2 : value2 }
# 键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dict = {'name': 'yl', 'Age': 7, 66: 'First'}
# 访问元素  dist[key]
print(dict['name'])
print(dict[66])
# 添加修改  del删除
# 键值重复会取后一个

# dict.keys()      返回包含字典所有 键 的可迭代对象
# dict.values()    返回包含字典所有 值 的可迭代对象
# dict.items()     返回包含字典所有 键：值 的可迭代对象
# dict.popitem(key)    删除字典最后一个 键值对


'''
chr(x)

将一个整数转换为一个字符

ord(x)

将一个字符转换为它的整数值

hex(x)

将一个整数转换为一个十六进制字符串

oct(x)

将一个整数转换为一个八进制字符串
'''