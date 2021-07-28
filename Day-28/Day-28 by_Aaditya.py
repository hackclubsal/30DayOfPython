#Day28_Challenge

def search(m, x):
    if(len(m) == 0):
        return -1

    for i in range(len(m)):
        for j in range(len(m)):

            if(m[i][j] == x):
                return True

    return False

m = [[1, 2, 3, 4], [11, 22, 37, 78], [23, 89, 12, 79 ], [43, 99, 29, 5]]
x = int(input("This is our goal:  "))

print(search(m, x))
