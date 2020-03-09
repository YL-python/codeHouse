ndarray = [13, 245, 342, 5345, 7645, 2354, 456, 2345, 345, 234, 63, 234, 6423]

for i in range(len(ndarray) - 1):
    for j in range(len(ndarray) - i - 1):
        if ndarray[j] > ndarray[j + 1]:
            ndarray[j], ndarray[j + 1] = ndarray[j + 1], ndarray[j]

print(ndarray)
