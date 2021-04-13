"""
Концепция следующая
если сумма 2-х сторон больше 3-й для всех комбинаций, то треугольник можно собрать
остальное как в школе
"""
a = int(input("Enter first length:\n"))
b = int(input("Enter second length:\n"))
c = int(input("Enter third length:\n"))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle!")
    if (a == b and a == c):
        print("Equilateral!")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Isosceles!")
    else:
        print("Versatile!")
else:
    print("Not triangle!")