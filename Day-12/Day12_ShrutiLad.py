n = int(input('Enter number of elements: '))
arr = []

for i in range (0,n):
    arr.append(int(input('Enter element: ')))
print(arr)

k = int(input('Enter the element you want to search: '))

def LinearSearch(k, arr):
    if k in arr: print("Index of element", k, "is", arr.index(k))
    else: print(-1)
LinearSearch(k, arr)  
