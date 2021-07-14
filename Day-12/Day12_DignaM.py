# Day-12_Hackclubsal_30DayOfPython_Solution
#Linear Search Operation in an Array.

num=int(input("Enter size of array:"))
arr=[]
j=0
flag=0
for i in range(0,num):
    x=int(input("Enter element :"))
    arr.append(x)
print(arr)
y=int(input("Enter Element you want to search:"))
for j in range(len(arr)):
    if(arr[j]==y):
        print(j)
        flag=1
if flag==0:
    print(-1)
