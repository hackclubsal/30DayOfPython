def binary_search(l,x):
    start=0
    end=len(l)-1
    
    if(len(l)>1):
        mid=(start+end)//2
        
        if(x==l[mid]):
            print(mid)
        
        else:
            
            if(x>l[mid]):
                l=l[mid+1:end+1]
            
            else:
                l=l[start:mid]
            
            return binary_search(l,x)
    
    if (l[start]==x) or (l[end]==x) :
        print(start)
    
    else:
        print('-1')

n=int(input('Enter the Size of your List: '))

l=[]

for i in range(n):
    l.append(int(input(f'Enter Numner {i+1}: ')))

print(binary_search(l,x=int(input("Enter the Value to be found: "))))