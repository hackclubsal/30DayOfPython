from time import clock
n,k=[int(i) for i in input("Enter size of list (N) and searching element(k) nmber:- ").split()]

flag=0;
listOfElement=[]

print('Enter element of array:- ')
for i in range(n):
    ele=int(input())
    listOfElement.append(ele)


flag=0   
print('Now search key element by Linear Search')    
start=clock()
for i in range(n):
    if(listOfElement[i]==k):
        flag=1
        break
end=clock()
if(flag):
    print("{} found at index {} and total time taken by Linear Search is {}".format(k,i,end-start))
else:
    print("{} not found -1 and total time taken by Linear Serarch is {}".format(k,end-start))
    
print('Now Serarch key by two pointer apporach')
loflag=0
hiflag=0
lo=0
hi=n-1
ind=-1

start=clock()
while(lo<=hi):
    if(listOfElement[lo]==k):
        loflag=1
        ind=lo
        break;
        
    if(listOfElement[hi]==k):
        hiflag=1
        ind=hi
        break
    lo+=1 
    hi-=1
end=clock()
if(loflag):
    print("{} found at index {} and total time taken by two pointer Linear Search is {}".format(k,ind,end-start))
elif(hiflag):
    print("{} found at index {} and total time taken by two pointer Linear Search is {}".format(k,ind,end-start))
    
else:
    print("{} not found -1 and total time taken by Linear Serarch is {}".format(k,end-start))
    
print("AS Two pointer Linear search little bit more efficient than simple Linear Search")
    
    


    
