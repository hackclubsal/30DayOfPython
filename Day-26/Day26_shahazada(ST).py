#Brute Force Apporach for Maximum Subarray
def maxSubOn3(arr):

    maximum=0
    for i in range(n):
        for j in range(i,n):
            subsum=0
            for k in range(i,j):
                subsum+=arr[k];
            maximum=max(subsum,maximum)
    return maximum

def maxSubOn2(arr):
    maximum=0
    for i in range(n):
        subsum=0
        for j in range(i,n):
            subsum+=arr[j]
            maximum=max(maximum,subsum)    
    return maximum
    
if __name__ == '__main__':
    n=int(input("Enter the size of array:- "))
    intArray=[]
    print("Enter Element of integer list ")
    for i in range(n):
        ele=int(input())
        intArray.append(ele)
    option=input("Enter on2 for O(n^2) and on3 for O(n^3) time complexity Subarray:- ")
    if(option=='on2'):
        maxsum=maxSubOn2(intArray)
    elif(option=='on3'):
        maxsum=maxSubOn3(intArray)
    print("maximum sum of Subarray is {}".format(maxsum))
        
    
