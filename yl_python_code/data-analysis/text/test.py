y = int(input("请输入年份："))
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("闰年")
else:
    print("非闰年")
