"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
def calc_num(x):
        if x==0:
            return 1
        elif x>0:
            return pow(-1,x)*pow(2,(-1)*x)+calc_num(x-1)

n=int(input("enter n:\n"))
rez=calc_num(n)
print(f"{rez=}")
