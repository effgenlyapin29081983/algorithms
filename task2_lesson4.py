import timeit
import cProfile

HOLE = 0


def sieve_erat(n):
    sieve = [i for i in range(n)]

    sieve[1] = HOLE
    for i in range(2, n):
        if sieve[i] != HOLE:
            j = i + i
            while j < n:
                sieve[j] = HOLE
                j += i

    res = [item for item in sieve if item != HOLE]
    return res


#print(sieve_erat(100))

nums = 100
for ns in range(7):
    func_name = f"sieve_erat({nums})"
    print(f"{nums}  {timeit.timeit(func_name, number=1000, globals=globals())}")
    # print()
    nums *= 2

"""
100  0.0214052
200  0.0411584
400  0.10234000000000001
800  0.20897960000000002
1600  0.5069264
3200  0.9633014
6400  1.9254267000000003
"""

cProfile.run("sieve_erat(10000000)")

"""
         6 function calls in 5.846 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.090    0.090    5.846    5.846 <string>:1(<module>)
        1    0.387    0.387    0.387    0.387 task2_lesson4.py:18(<listcomp>)
        1    4.868    4.868    5.756    5.756 task2_lesson4.py:7(sieve_erat)
        1    0.501    0.501    0.501    0.501 task2_lesson4.py:8(<listcomp>)
        1    0.000    0.000    5.846    5.846 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

def erat(n):
    res = [i for i in range(n)]
    spam = res.pop(0)
    spam = res.pop(0)
    for i in range(len(res) - 1, 1, -1):
        j = 0
        while i > j:
            if res[i] % res[j] != 0:
                j += 1
            else:
                spam = res.pop(i)
                j = i + 1

    return res


#print(erat(100))

nums = 100
for ns in range(7):
    func_name = f"erat({nums})"
    print(f"{nums}  {timeit.timeit(func_name, number=1000, globals=globals())}")
    # print()
    nums *= 2

"""
100  0.1176630000000003
200  0.6149055000000008
400  1.5681764000000005
800  8.034808499999999
1600  28.228451999999997
3200  90.41251540000002
6400  342.18061320000004
"""


cProfile.run("erat(10000000)")

"""
Я очень долго ждал
"""

"""
Вывод:
Нахожение простых чисел по алгоритму "Решето Эратосфена"
более быстрый нежели
простой перебор массива и проверка на наличие делителей
"""