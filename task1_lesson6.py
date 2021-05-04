import sys
"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
def var1(x):
    sum = 0
    for el in range(1,x+1,1):
        sum+=el
    sum1 = x*(x+1)/2
    temp_arr = [1, 2, 3, 4]
    temp_arr1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    temp_set = (1,2,3,4,5)
    arr_vars = locals()
    size_vars = 0
    for el in arr_vars.keys():
        if hasattr(el, "__iter__"):
            for els in el:
                size_vars += sys.getsizeof(els)
        else:
            size_vars += sys.getsizeof(el)
    return sum == sum1, size_vars, arr_vars.keys()

    
n = int(input("Введите целое больше 0:\n"))
print(var1(n))

#python version 3.8.3
#OS Android 10
#IDE pyDroid

#Не было времени проверить 2 дополнительных варианта, но поигрался с добавлением новых переменных temp_arr =400, temp_set=400, temp_arr1=450
"""
компутер поломался
"""
