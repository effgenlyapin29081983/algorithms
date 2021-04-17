n=int(input("Количество символов=\n"))
f_num=int(input("Искомое число от 0 до 9=\n"))
k=0
num=0
while k<n:
    if f_num==int(input("Введите чило от 0 до 9:\n")):
        num+=1
    k+=1
print(f"Количество искомых={num}" )