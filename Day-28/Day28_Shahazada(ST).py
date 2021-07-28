''' In both the example matrix look sorted that's why  i  applied Binary Search '''

def binarySearchInMatrix(matrix,n,m,target):
    lo=0
    hi=n*m
    
    while(lo<=hi):
        mid=(lo+hi)//2
        
        if matrix[mid//m][mid%m]==target:
            return [mid//m,mid%m]
        elif matrix[mid//m][mid%m]>target:
            hi=mid-1
        else:
            lo=mid+1
    return 0


if __name__ == '__main__':
    n,m=input("Enter Dimension of matrix:- ").split()
    
    n=int(n)
    m=int(m)
    matrix=[]
    
    print("Enter element of matrix")
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(int(input()))
        matrix.append(row)    
    
    print("Your matrix")
    for i in range(n):
        for j in range(m):
           print(matrix[i][j],end=" ")
        print()   
            
    target=int(input("Enter Target number:- "))
    
    loc=binarySearchInMatrix(matrix,n,m,target)
    if(loc):
        print("{} found at {},{} in matrix ".format(target,loc[0],loc[1]))
    else:
        print("{} is not found in matirx ".format(target))
