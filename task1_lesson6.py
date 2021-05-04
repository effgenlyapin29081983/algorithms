import sys
"""
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
def var1(x):
    sum=0
    for el in range(1,x+1,1):
        sum+=el
    sum1=x*(x+1)/2
    return sum==sum1

def show_sizeof(x, level=0):
    print "\t" * level, x.__class__, sys.getsizeof(x), x
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)
    
n=int(input("Введите целое больше 0:\n"))
print(show_sizeof(var1(n)))
print(var1(n))
