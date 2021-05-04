import sys

"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def var1(x):
    summa = 0
    for el in range(1, x + 1, 1):
        summa += el
    summa1 = x * (x + 1) / 2
    arr_vars = locals()
    size_vars = 0
    for el in arr_vars.keys():
        if hasattr(arr_vars.get(el), "__iter__"):
            for els in arr_vars.get(el):
                size_vars += sys.getsizeof(els)
        else:
            size_vars += sys.getsizeof(arr_vars.get(el))
    return summa == summa1, size_vars, arr_vars.keys()


def var2(x):
    arr_els = {i for i in range (1, x+1)}
    summa = sum(arr_els)
    summa1 = x * (x + 1) / 2
    arr_vars = locals()
    size_vars = 0
    for el in arr_vars.keys():
        if hasattr(arr_vars.get(el), "__iter__"):
            for els in arr_vars.get(el):
                size_vars += sys.getsizeof(els)
        else:
            size_vars += sys.getsizeof(arr_vars.get(el))
    return summa == summa1, size_vars, arr_vars.keys()


def var3(x):
    arr_els = [i for i in range (1, x+1)]
    summa = sum(arr_els)
    summa1 = x * (x + 1) / 2
    arr_vars = locals()
    size_vars = 0
    for el in arr_vars.keys():
        if hasattr(arr_vars.get(el), "__iter__"):
            for els in arr_vars.get(el):
                size_vars += sys.getsizeof(els)
        else:
            size_vars += sys.getsizeof(arr_vars.get(el))
    return summa == summa1, size_vars, arr_vars.keys()


n = int(input("Введите целое больше 0:\n"))
print(var1(n))
print("-----------------------------------------------------------------------------------------")
print(var2(n))
print("-----------------------------------------------------------------------------------------")
print(var3(n))

# python version 3.8.3
# OS Android 10
# IDE pyDroid

# Список и множество занимают одинаковое количество байт памяти
"""
(True, 108, dict_keys(['x', 'summa', 'el', 'summa1']))
-----------------------------------------------------------------------------------------
(True, 640, dict_keys(['x', 'arr_els', 'summa', 'summa1']))
-----------------------------------------------------------------------------------------
(True, 640, dict_keys(['x', 'arr_els', 'summa', 'summa1']))
"""
