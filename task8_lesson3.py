"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

COUNT_ROWS = 5
COUNT_COLS = 4

matrix = []
for i in range(COUNT_ROWS):
    sum_row = 0
    matrix.append([])
    for j in range(COUNT_COLS-1):
        matrix[i].append(float(input(f"Введите {j} элемент {i} строки: ")))
        sum_row += matrix[i][j]
    matrix[i].append(sum_row)
for i in range(len(matrix)):
    print(f"{matrix[i]}")
