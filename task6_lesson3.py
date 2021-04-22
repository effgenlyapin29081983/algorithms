"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

LENGTH_LIST = 10
MIN_VALUE = 0
MAX_VALUE = 100_000
DIVISOR = 1000

src_list = [randint(MIN_VALUE, MAX_VALUE)/DIVISOR for _ in range(LENGTH_LIST)]
print(src_list)

min_ind = 0
max_ind = 0

for i in range(len(src_list)):
    if src_list[i] > src_list[max_ind]:
        max_ind = i
    elif src_list[i] < src_list[min_ind]:
        min_ind = i

beg_ind = end_ind = 0

if min_ind < max_ind:
    beg_ind = min_ind+1
    end_ind = max_ind

elif min_ind > max_ind:
    beg_ind = max_ind + 1
    end_ind = min_ind

sum_els = 0
for i in range(beg_ind, end_ind):
    sum_els += src_list[i]

print(f"{sum_els}")
