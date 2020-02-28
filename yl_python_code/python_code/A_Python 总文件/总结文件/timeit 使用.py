# import copy
#
#
# def test_copy(inv):
#     return copy.copy(inv)
#
#
# def test_deepcopy(inv):
#     return copy.deepcopy(inv)
#
#
# dct = {str(i): i for i in range(100)}
#
#
# def timeit_copy():
#     from timeit import timeit
#     print(timeit('mian().test_copy(dct)', 'from __main__ import test_copy, dct'))
#     print(timeit('test_deepcopy(dct)', 'from __main__ import test_deepcopy, dct'))
#
#
# if __name__ == '__main__':
#     timeit_copy()
from timeit import timeit
import copy
c =[1,2,3,4,5,[1,2,3,4]]
print(timeit('copy.copy({})'.format(c),'import copy'))