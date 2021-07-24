# Day-23 Question for the day-23 is --->

# -> Question:  Write a program to cyclically rotate an array by two

# -> Input: 
# N= 4, [1, 54, 32, 12]

# -> Output:-
# [12, 32, 1, 54]

# -> Input:-
# N= 6, [1, 2, 3, 4, 5, 6]

# -> Output:- 
# [6, 5, 1, 2, 3, 4]



if __name__ == '__main__':
    n=int(input("Enter the size of list : "))
    print("Enter element of list : ")
    elementList=[]
    for i in range(n):
        ele=int(input())
        elementList.append(ele)
    
    rotatedlist=[]    
    for i in range(n-1,n-3,-1):
        rotatedlist.append(elementList[i])
    
    for i in range(n-2):
        rotatedlist.append(elementList[i])
    print()   
    print("Rotated cyclically list element are : ",end=" ")
    for i  in range(n):
        print(rotatedlist[i],end=" ")
        
        
        
        
