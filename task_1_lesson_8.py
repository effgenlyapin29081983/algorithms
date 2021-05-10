import hashlib
"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. 
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком
"""
def find_unique_substr(s):
    hash_str = []
    for i in range(0, len(s)):
        for j in range(i,len(s)):
            hash_str.append(hashlib.sha1(s[i:j+1].encode('UTF-8')).hexdigest())
    hash_set = set(hash_str)
    return len(hash_set)-1

inp_str = input("Enter string:\n")
print(f"{find_unique_substr(inp_str)}")
