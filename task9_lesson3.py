"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

COUNT_ROWS = 5
COUNT_COLS = 4
MIN_VALUE = 0
MAX_VALUE = 100_000
DIVISOR = 1000


min_els = []
matrix = []
for i in range(COUNT_ROWS):
    matrix.append([])
    min_el_col = 0
    for j in range(COUNT_COLS):
        matrix[i].append(randint(MIN_VALUE, MAX_VALUE)/DIVISOR)
        if j == 0:
            min_el_col = matrix[i][j]
        else:
            if matrix[i][j] < min_el_col:
                min_el_col = matrix[i][j]
    min_els.append(min_el_col)

for i in range(COUNT_COLS):
    print([matrix[j][i] for j in range(COUNT_ROWS)])

print(min_els)

max_el = min_els[0]
for i in range(1, len(min_els)):
    if min_els[i] > max_el:
        max_el = min_els[i]
print(f"{max_el}")
