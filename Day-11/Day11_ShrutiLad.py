n=int(input("Enter n"))
t1=1
t2=0

for i in range(1,n+1):
    t3=t1+t2
    t1=t2
    t2=t3
print(n,"th number of Fibonacci series is ",t3)
