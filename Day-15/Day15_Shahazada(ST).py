'''
best time complexity O(nlogn)
worst time complexity O(n^2)
'''

def partition(elementList,start,end):
    pivotIndex=start #index of left most element as pivot index we can use other than start also
    pivot=elementList[pivotIndex] #choose pivot element
    
    
    while start<end:  
        while start<len(elementList) and elementList[start]<=pivot:
            start+=1
        while elementList[end]>pivot:
            end-=1
    
        if(start<end):
            elementList[start],elementList[end]=elementList[end],elementList[start]
    
    
    elementList[pivotIndex],elementList[end]=elementList[end],elementList[pivotIndex] #swap end's  with pivot's index 
    return end #return pivot index
    
def quickSort(elementList,start,end):
    if(start<end):
        pi=partition(elementList,start,end) #return pivot at correct position
        quickSort(elementList,start,pi-1) #left half
        quickSort(elementList,pi+1,end)   #right half
    
    

if __name__ == '__main__':
    n=int(input("Enter size of elementLst:- "))
    
    print("Enter element of elementList")
    
    elementList=[]
    for i in range(n):
        ele=int(input())
        elementList.append(ele)
    quickSort(elementList,0,len(elementList)-1)
    print(elementList)
        
