operations = {"+","-","*","/"}
while True:
    op=input("operation '+,-,/,*', 0 - exit\n")
    if op in operations:
        a=int(input("enter firtst\n"))
        b=int(input("enter second\n"))
        if op == "+":
            print(f"{a+b=}")
        elif op =="-":
            print(f"{a-b=}")
        elif op == "*":
            print(f"{a*b=}")
        elif op =="/":
            if b == 0:
                print("Division by zero")
            else:
                print(f"{a/b=}")
    elif op=="0":
        print("Exit\n")
        break
    else:
        print("Wrong operation\n")
