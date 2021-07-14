def bubbleSort(element,n):
    
    for i in range(n):
        swapped=True
        for j in range(n-i-1):
            if(element[j]>element[j+1]):
                element[j],element[j+1]=element[j+1],element[j]
                swapped=False
        if(swapped):
            break;



if __name__ == '__main__':
    n=int(input("Enter size of list:- "))
    
    elementList=[]
    print('Enter element into elementList')
    for i in range(n):
        ele=int(input())
        elementList.append(ele)
    print("If list is already sorted then it's timecomplexity will be O(n) other wise O(n^2)")
    
    bubbleSort(elementList,n)    
    
    for i in range(n):
        print(elementList[i],end=' ')


