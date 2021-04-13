"""
Используется получение кода символа в Юникоде
a - z = 97 - 122
"""
a = input("Enter first char :\n")
b = input("Enter second char:\n")

print("code(a) = ", ord(a) - 96)
print("code(b) = ", ord(b) - 96)
print("Count chars between a and b = ", abs(ord(a)-ord(b)) - 1)