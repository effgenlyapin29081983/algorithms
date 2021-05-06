import random

"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100,100).
Выведете на экран исходный и отсортированный массивы
"""

SIZE_ARRAY = 20
MIN_DIAPAZON = -100
MAX_DIAPAZON = 100

def sort_bubble(data):
    n = 1
    while n<len(data):
        for i in range(len(data)-n):
            if data[i] < data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
        n += 1


rand_array = []
for i in range (SIZE_ARRAY):
    rand_array.append(random.randint(MIN_DIAPAZON,MAX_DIAPAZON - 1))
print(rand_array)
sort_bubble(rand_array)
print(rand_array)
