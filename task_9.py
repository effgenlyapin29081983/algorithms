a=int(input("Введите a:\n"))
b=int(input("Введите b:\n"))
c=int(input("Введите c:\n"))

if (a>b):
    if (a>c):
        if(b>c):
            print("Среднее b,",b)
        else:
            print("Среднее c,",c)
    else:
        print("Среднее a,",a)
else:
    if (b>c):
        if(a>c):
            print("Среднее a,",a)
        else:
            print("Среднее c,",c)
    else:
        print("Среднее b,",b)