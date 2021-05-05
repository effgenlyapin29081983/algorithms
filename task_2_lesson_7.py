import random
SIZE_ARRAY = 20
MIN_DIAPAZON = 0
MAX_DIAPAZON = 50

def merge(data, left, mid, right):
    it1 = 0
    it2 = 0
    result = []
    for i in range (right - left):
        result.append(0)
  
    while left + it1 < mid and mid + it2 < right:
        if data[left + it1] < data[mid + it2]:
            result[it1 + it2] = data[left + it1]
            it1 += 1
        else:
            result[it1 + it2] = data[mid + it2]
            it2 += 1
    #print(f"result1 = {result}")
    while left + it1 < mid:
        result[it1 + it2] = data[left + it1]
        it1 += 1
    #print(f"result2 = {result}")
    while mid + it2 < right:
        result[it1 + it2] = data[mid + it2]
        it2 += 1
    #print(f"result3 = {result}")
    for i in range (it1 + it2):
        data[left + i] = result[i]
    #print(f"data1 = {data}")
    
#def mergeSortRecursive(data, left, right):
#    if (right - left) <= 1:
#        return
#    mid = (right-left) // 2
#    mergeSortRecursive(data, left, mid)
#    mergeSortRecursive(data, mid, right)
#    merge(data, left, mid, right)

def mergeSortIterative(data):
    for i in range(len(data)-1,1,-1): 
        for j in range (0, len(data) - i):
            merge(data, j, j + i, min(j + 2 * i, len(data)))
            print(f"data = {data}")
            j += 2 * i
        i *= 2

array_data = []
for i in range (SIZE_ARRAY):
    array_data.append(random.randint(0,50))
    #array_data.append(MIN_DIAPAZON + (MAX_DIAPAZON - MIN_DIAPAZON) * random.random())
#array_data = [63.5, -66.3, 34.2, -65.3, -39.7, -75.4, 94.2, 90.3, -78.7, -20.1, -30.2, 4.5, -31.7, 2.1, -70.8, 24.2, -77.6, -92.3, -57.8]
print(array_data)
#mergeSortRecursive(array_data, 0, len(array_data))
mergeSortIterative(array_data)
print(array_data)
