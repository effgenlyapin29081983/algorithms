from collections import deque

NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

def sum_hex(a, b):
    lst_a = deque(a)
    lst_b = deque(b)
    if len(lst_a) > len(lst_b):
        len_diff = len(lst_a) - len(lst_b)
        for ld in range(1, len_diff + 1):
            lst_b.appendleft('0')
    else:
        len_diff = len(lst_b) - len(lst_a)
        for ld in range(1, len_diff + 1):
            lst_a.appendleft('0')
    res = deque([0])
    count = 1
    
    for i in range(len(lst_a)-1, -1, -1):
        res.appendleft(0)
        spam = res[len(res)-count] + NUMBERS.index(lst_a[i]) + NUMBERS.index(lst_b[i])
        res[len(res)-count] = spam % 16
        if spam > 15:
            res[len(res)-count-1] = spam // 16
        count +=1
    if res[0] == 0:
        res.popleft()
    for i in range(0,len(res)):
        res[i] = NUMBERS[res[i]]
    return ''.join(res)


def mul_hex(a, b):
    lst_a = deque(a)
    lst_b = deque(b)
    result = "0"
    
    
    count_b = 1
    
    for i in range(len(lst_b)-1, -1, -1):
        res = deque([0])
        count_a = 1
        for j in range(len(lst_a)-1, -1, -1):
            res.appendleft(0)
            spam = res[len(res)-count_a] + NUMBERS.index(lst_a[j]) * NUMBERS.index(lst_b[i])
            res[len(res)-count_a] = spam % 16
            if spam >= 15:
                res[len(res)-count_a-1] = spam // 16
            count_a +=1
        for nulls in range(0, count_b-1):
            res.append(0)
        if res[0] == 0:
            res.popleft()
        for ind in range(0,len(res)):
            res[ind] = NUMBERS[res[ind]]
        eggs = ''.join(res)
        result = sum_hex(result, eggs)
        count_b += 1
    return result


first_num = input("Enter first num (using chars in [0..A]):\n")
second_num = input("Enter second num (using chars in [0..A]):\n")

print("sum :")
print(sum_hex(first_num, second_num))
            
print("mul :")
print(mul_hex(first_num, second_num))