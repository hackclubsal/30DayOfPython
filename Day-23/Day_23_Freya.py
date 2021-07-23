#program to cyclically rotate an array by two
n=int(input("enter size of array"))
array=[]
for i in range(0,n):
    x=int(input("enter element"))
    array.append(x)
print("Before rotation:",array)
def rotate(array):
   y=array.pop()
   array.insert(0,y)
for i in range(2): #to perform rotation twice
 rotate(array)
print("After two rotations:",array)
