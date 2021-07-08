# # Basic
m=int(input("Enter the Starting value: "))
n=int(input("Enter the Ending value: "))
sum=0
for i in range(m+1,n):
    if(i%2==0):
       sum+=i
print(sum)

# List comprehension
sum=0
l=[i for i in range(int(input("Enter the Starting value: "))+1,int(input("Enter the Ending value: "))) if(i%2==0)]
for i in l:
    sum+=i
print(sum)