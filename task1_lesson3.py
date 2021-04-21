"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

MIN_DIAPAZON = 2
MAX_DIAPAZON = 99
MIN_DIVISOR = 2
MAX_DIVISOR = 9

array_of_multiple=[]
for el in range(MIN_DIVISOR, MAX_DIVISOR+1):
    array_of_multiple.append(MAX_DIAPAZON//el)
print(array_of_multiple)