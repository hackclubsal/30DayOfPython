if __name__ == '__main__':
    n,m=input("Enter  the dimension of matrix:- ").split()
    n=int(n)
    m=int(m)
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(m):
            ele=int(input())
            row.append(ele)
        matrix.append(row)
    
    print("Your entered matrix is ")
    
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],end=" ")
            
        print()
    print("Lower matrix of given matrix ")
    
    for i in range(n):
        for j in range(m):
            if j>i:
                matrix[i][j]=0
    
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],end=" ")
        
        print()    
            
