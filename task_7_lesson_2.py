"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
n=int(input("Введите целое больше 0:\n"))
sum=0
for el in range(1,n+1,1):
    sum+=el
sum1=n*(n+1)/2
if sum==sum1:
    print(f"{sum} == {sum1}")
else:
    print(f"{sum} <> {sum1}")
