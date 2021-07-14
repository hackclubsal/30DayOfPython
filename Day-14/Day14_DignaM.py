# Day-14_Hackclubsal_30DayOfPython_Solution
# Program to Perform a Bubble Sort Algorithm in a Python .


def bubble_sort(arr):
    flag=False
    while(flag!=True):
        count=0
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                count+=1
        if(count==0):
            flag=True
    return arr

n=int(input("Enter the Size of Array:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter Element number {i+1}: ")))
print(bubble_sort(arr))
