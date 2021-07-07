'''
# split() convert str to list and it's deafult separator is space
n,m=input().split() #take input in same line  
n=int(n) #by  default in python input in str form  that's why convert it into explicitly int form
m=int(m)
'''
n,m=[int(x) for x in input().split()] #take input both  in same line  from user and convert str list element to integer element into integer
n+=1 #increm,ent n by 1
while(n<m): #loop run until not equalt(less than ) to m
    if(n+1==m):
        print(n)
    else:
        print(n,end=',') #print n set end=', ' for output in same line 1,2,3 ,by default end is set by break line char (\n ) 
    n+=1 #incremetn n for reaching condition n==m,then 
    