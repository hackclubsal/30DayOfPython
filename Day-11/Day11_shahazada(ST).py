print("if n start from 1 then the terms f(n) of fibonacci is following:-\n f(1)=1, f(2)=1, f(3)=2, f(4)=3, f(5)=5, f(6)=8, f(7)=13\n")

nth=int(input('Enter your term:- '))
a=1
b=1
c=1
if(nth==1 or nth==2):
    print(c)

else:
    while(nth>2):
        c=a+b
        a=b
        b=c
        nth-=1
    print(c)    
