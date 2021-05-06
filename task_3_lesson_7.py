import random
MIN_DIAPAZON = 0
MAX_DIAPAZON = 100

"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""


arr_src = []

m = int(input("Введите число m:\n"))

for i in range (2*m+1):
    arr_src.append(MIN_DIAPAZON + (MAX_DIAPAZON - MIN_DIAPAZON) * random.random())
print(arr_src)

minHeap = []

i = 0
half_length = len(arr_src) // 2
while i <= half_length:
    min_el = min(arr_src)
    minHeap.append(min_el)
    arr_src.remove(min_el)
    i += 1

print(f"Mediana = {minHeap[len(minHeap)-1]}")
