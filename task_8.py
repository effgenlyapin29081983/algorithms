a = int(input("Введите год\n"))
if (a % 4 != 0) or (a % 100 == 0 and a % 400 != 0):
    print("Обычный")
else:
    print("Високосный")
