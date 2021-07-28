#day28
m = int(input("Number of rows: "))
n = int(input("Number of columns: "))
matrix = []
print("Enter the elements row-wise: ")
result = False
for i in range (0, m):
    x = []
    for j in range (0, n):
        x.append(int(input()))
    matrix.append(x)
target = int(input("Enter target element: "))
for i in range (0, m):
    for j in range (0, n):
        if(matrix[i][j] == target):
              result = True
print(result) 
