#Day-23_Hackclubsal_30DayOfPython_Solution
#Program to Cyclically rotate an arr by two

num = int(input("Enter size of arr : \n"))
arr = []

for i in range(0,num):
    k = int(input("Enter element : \n"))
    arr.append(k)
print("Before rotation:",arr)

def rotate(arr):
    x = arr.pop()
    arr.insert(0,x)
for i in range(2): 
    rotate(arr)
print("After two rotations:",arr)
