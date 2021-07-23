n = int(input('Enter number of elements: '))
arr = []

for i in range (0, n):
    x = int(input('Enter element: '))
    arr.append(x)

print('Before rotation', arr)

def rotate(arr):
    x = arr.pop()
    arr.insert(0, x)

for i in range(2):
    rotate(arr)

print('After 2 rotations', arr)
