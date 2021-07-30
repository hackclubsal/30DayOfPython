R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")


def lower(matrix, row, col):

    for i in range(0, row):

        for j in range(0, col):

            if (i < j):

                print("0", end=" ")

            else:
                print(matrix[i][j], end=" ")

        print(" ")


for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
print()
lower(matrix, R, C)
