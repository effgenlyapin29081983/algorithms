import random
SIZE_ARRAY = 20
MIN_DIAPAZON = 0
MAX_DIAPAZON = 50

"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
"""
Честно, взял псевдокод отсюда и доработал))) Мой любимый универ!!!
https://neerc.ifmo.ru/wiki/index.php?title=%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC
"""

def merge(data, left, mid, right):
    it1 = 0
    it2 = 0
    result = []
    for i in range (right - left):
        result.append(0)
  
    while left + it1 < mid and mid + it2 < right:
        if data[left + it1] < data[mid + it2]:
            result[it1 + it2] = data[left + it1]
            it1 += 1
        else:
            result[it1 + it2] = data[mid + it2]
            it2 += 1
    
    while left + it1 < mid:
        result[it1 + it2] = data[left + it1]
        it1 += 1
    
    while mid + it2 < right:
        result[it1 + it2] = data[mid + it2]
        it2 += 1

    for i in range (it1 + it2):
        data[left + i] = result[i]

    

def mergeSortIterative(data):
    for i in range(len(data)-1,0,-1): 
        for j in range (0, len(data) - i):
            merge(data, j, j + i, min(j + 2 * i, len(data)))
            j += 2 * i
        i *= 2

array_data = []
for i in range (SIZE_ARRAY):
    array_data.append(MIN_DIAPAZON + (MAX_DIAPAZON - MIN_DIAPAZON) * random.random())
print(array_data)
mergeSortIterative(array_data)
print(array_data)
