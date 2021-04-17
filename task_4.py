def calc_num(x):
        if x==0:
            return 1
        elif x>0:
            return pow(-1,x)*pow(2,(-1)*x)+calc_num(x-1)

n=int(input("enter n:\n"))
rez=calc_num(n)
print(f"{rez=}")