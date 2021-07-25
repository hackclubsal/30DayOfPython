#Brute  force apporach fro Two Sum Problem
def twoSumOn2(arr,target):
    ans=[]
    flag=True
    for i in range(len(arr)-1):
        diffTarget=target-arr[i]
        for j in range(len(arr)):
            if arr[j]==diffTarget:
                ans.append(i)
                ans.append(j)
                return ans

#optimized method of Two Sum Problem
def twoSumOn(arr,target):
    ans={}
    for i in range(len(arr)):
        if target-arr[i] in ans:
            return [ans[target-arr[i]],i]
        ans[arr[i]]=i    
 
if __name__ == '__main__':
    n=int(input("Enter size of integer array:- "))
    arr=[]
    print("Enter element of integer array ")
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    target=int(input("enter Target element which is sum of two element:- "))
    
    option=input("For solution in O(n)  and O(n^2) Enter n ans n2 respectively:- ").split()
    option=option[0].lower()
    
    if option=='n':
        print("::::This soultion in O(n) time Complexity::::")
        myans=twoSumOn(arr,target)
    elif option=='n2':
        print("::::This soultion in O(n^2) time Complexity::::")
        myans=twoSumOn2(arr,target)
        
    for i in myans:
        print(i,end=" ,")
        
    
