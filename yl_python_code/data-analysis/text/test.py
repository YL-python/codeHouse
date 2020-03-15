x = 1
y = 1
z = 1

x = y = z = 1

#  x = (y = z + 1)

x, y = y, x

x += y

x = 4.5

y = 2

print(x//y)

x = 1
y = 0
z = 0

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)