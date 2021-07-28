
def search(mat, x):
    if(len(mat) == 0):
        return -1

    for i in range(len(mat)):
        for j in range(len(mat)):

            if(mat[i][j] == x):
                return True

    return False


mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
x = int(input("Target :  "))
# print(mat)
print(search(mat, x))
