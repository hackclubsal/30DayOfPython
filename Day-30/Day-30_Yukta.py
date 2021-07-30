N = int(input("Enter the number of rows :"))
M = int(input("Enter the number of columns :"))

matrix = []
print("Enter elements row-wise:")

for i in range(N):          # A for loop for row entries
    a =[]
    for j in range(M):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
print("Lower triangular matrix -")
for i in range(0, N):
    for j in range(0, M):
        if(j > i):
            print("0", end = " ")
        else:
            print(matrix[i][j],
                       end = " " )
    print()