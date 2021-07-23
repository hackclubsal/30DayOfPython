'''This program rotate list cyclically by user choice'''

if __name__ == '__main__':
    n=int(input("Enter the size of list:- "))
    print("Enter element of list")
    elementList=[]
    for i in range(n):
        ele=int(input())
        elementList.append(ele)
    
    rotatedlist=[]    
    rotateBy=int(input("By how many element want to rotate:- "))
    for i in range(n-1,n-rotateBy-1,-1):
        rotatedlist.append(elementList[i])
    
    for i in range(n-rotateBy):
        rotatedlist.append(elementList[i])
    print()   
    print("Rotated cyclically list element are :-",end=" ")
    for i  in range(n):
        print(rotatedlist[i],end=" ")
        
        
        
        
