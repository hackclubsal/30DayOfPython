n = int(input('Enter number: '))
arr = []

for i in range (0, n):
    x = int(input('Enter element: '))
    arr.append(x)

def BubbleSort(arr):
    l = len(arr)
    for i in range(0, l-1):
        for j in range(0, l-1-i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

BubbleSort(arr)
print("The sorted array is:", arr)
