arr = []
flag=0 

n = int(input("Enter number of elements : "))
k = int(input("Enter the element to be searched : ")) 

for i in range(0, n):
    ele = int(input())
 
    arr.append(ele) 
     
#print(arr)

for i in range(0, n):
    if(arr[i]==k):
        print("Element is found at index position : ",i)
       
        flag = 1
    
if(flag==0):
        print("Element not found")