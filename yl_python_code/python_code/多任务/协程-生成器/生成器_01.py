 # 生成器是一种特殊的迭代器
 # 吧列表推导式的 [] 变成()

# 都可以用 for 区别在第一个nums1用到了内存空间 第二个nums2不占内存

nums1 = [x*2 for x in range(10)]
print(nums)

nums2 = (x*2 for x in range(10))
print(nums2)
for i in nums2:
    print(i,end='  ')