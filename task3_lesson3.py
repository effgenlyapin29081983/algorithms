"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

LENGTH_LIST = 10
MIN_VALUE = 0
MAX_VALUE = 100

src_list = [randint(MIN_VALUE,MAX_VALUE) for _ in range(LENGTH_LIST)]
print(src_list)

min_ind = 0
max_ind = 0

for i in range(len(src_list)):
    if src_list[i] > src_list[max_ind]:
        max_ind = i
    elif src_list[i] < src_list[min_ind]:
        min_ind = i

src_list[max_ind], src_list[min_ind] = src_list[min_ind], src_list[max_ind]

print(src_list)
