def binarySearch(elementList,n,k):
    hi=n-1
    lo=0
    
    while(lo<=hi):
        mid=(lo+hi)//2
        
        if(elementList[mid]==k):
            print(mid)
            return mid
        elif(elementList[mid]>k):
            hi=mid-1
        else:
            lo=mid+1
    return -1        
    
    

if __name__=='__main__':
    n,k=[int(i) for i in input("Enter n and k:- ").split()]
    
    elementList=[]
    print("Enter element of list:-")
    for i in range(n):
        ele=int(input())
        elementList.append(ele)
    ans=binarySearch(elementList,n,k)    
    
    if(ans==-1):
        print("{} not found in the list".format(k))
    else:
        print("{} found at index {} in the list".format(k,ans))
    
    
