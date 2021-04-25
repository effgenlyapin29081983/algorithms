"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

import timeit
import cProfile

MIN_DIVISOR = 2
MAX_DIVISOR = 9


def f_multiples(n):
    array_of_multiple = []
    for el in range(MIN_DIVISOR, MAX_DIVISOR + 1):
        array_of_multiple.append(n // el)
    return array_of_multiple


nums = 100
for ns in range(10):
    func_name = f"f_multiples({nums})"
    print(f"{nums}  {timeit.timeit(func_name, number=1000, globals=globals())}")
    # print()
    nums *= 2
"""
100  0.0008355999999999988
200  0.0008182000000000016
400  0.0008254999999999998
800  0.0008644000000000013
1600  0.0008705999999999992
3200  0.000893999999999999
6400  0.0008927999999999991
12800  0.0008893000000000026
25600  0.0009189000000000003
51200  0.0009408999999999945
"""

cProfile.run("f_multiples(10000000)")

"""
         12 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task4_lesson1.py:12(f_multiples)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def f_multiples_arr(n):
    array_of_multiple = [0, 0, 0, 0, 0, 0, 0, 0]
    for el in range(2, n + 1):
        for numbrs in range(MIN_DIVISOR, MAX_DIVISOR + 1):
            if (el % numbrs == 0):
                array_of_multiple[numbrs - 2] += 1
    return array_of_multiple


nums = 100
for ns in range(10):
    func_name = f"f_multiples_arr({nums})"
    print(f"{nums}  {timeit.timeit(func_name, number=1000, globals=globals())}")
    # print()
    nums *= 2

"""
100  0.0912992
200  0.21664289999999997
400  0.2673003
800  0.8435276
1600  1.0981169000000002
3200  2.4640883000000002
6400  5.6926499
12800  10.157899500000001
25600  20.3842238
51200  40.17959079999999
"""

cProfile.run("f_multiples_arr(10000000)")

"""
         4 function calls in 8.707 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.707    8.707 <string>:1(<module>)
        1    8.707    8.707    8.707    8.707 task4_lesson1.py:64(f_multiples_arr)
        1    0.000    0.000    8.707    8.707 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def f_multiples_arr2(n):
    array_of_multiple = []
    for numbrs in range(MIN_DIVISOR, MAX_DIVISOR + 1):
        multiple = 0
        for el in range(2, n + 1):
            if (el % numbrs == 0):
                multiple += 1
        array_of_multiple.append(multiple)
    return array_of_multiple

nums = 100
for ns in range(10):
    func_name = f"f_multiples_arr2({nums})"
    print(f"{nums}  {timeit.timeit(func_name, number=1000, globals=globals())}")
    # print()
    nums *= 2

"""
100  0.05217589999999994
200  0.1548202999999999
400  0.1880001
800  0.3257606000000006
1600  0.709283300000001
3200  1.4395375999999995
6400  2.8424902000000003
12800  5.887978500000001
25600  12.802972
51200  25.1082617
"""

cProfile.run("f_multiples_arr(10000000)")

"""
         4 function calls in 9.350 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    9.350    9.350 <string>:1(<module>)
        1    9.350    9.350    9.350    9.350 task4_lesson1.py:54(f_multiples_arr)
        1    0.000    0.000    9.350    9.350 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
Вывод:
Оптимальное решение задачи - n//2
время исполнения одинаково, независимо от n (O(n))
"""