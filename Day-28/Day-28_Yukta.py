m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []
print("Enter the elements row-wise-")
b = False
for i in range (0, m):
    a = []
    for j in range (0, n):
        a.append(int(input()))
    matrix.append(a)

target = int(input("Enter element to be searched: "))

for i in range (0, m):
    for j in range (0, n):
        if(matrix[i][j] == target):
              b = True
        
print(b)