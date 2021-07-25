n = int(input('Enter number of elements: '))
arr = []

for i in range (0, n):
    x = int(input('Enter element: '))
    arr.append(x)

target = int(input('Enter sum of two numbers: '))

def checkSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == target:
                return i, j 
    return 0


if (checkSum(arr, target) == 0):
    print('target  not found')
else:
    print(checkSum(arr, target))
