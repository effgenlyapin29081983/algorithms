"""
В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. 
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

from random import randint

x=randint(0,101)
it=0
while it<10:
    en_num=int(input("Введите число от 0 до 100\n"))
    it+=1
    if en_num==x:
        print(f"Число угадано и равно {en_num}")
        break
    elif en_num>x:
        print(f"Загаданное число < {en_num}")
    else:
        print(f"Загаданное число > {en_num}")
print(f"Было загадано {x}")
