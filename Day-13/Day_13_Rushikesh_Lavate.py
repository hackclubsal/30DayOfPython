def BinarySearch(l,k):
    l.sort()
    n=len(l)
    # Apply Binary Search
    # first sort the list/array
    start = 0
    last = n-1
    if n>1:
        mid = ((start+last)//2)+1
        if k == l[mid]:
            print(mid)
        elif(k>l[mid]):
            l = l[mid+1:]
            return BinarySearch(l,k)
        else:
            l = l[:mid]
            return BinarySearch(l, k)
    else:
        print(-1)

def CreateList(n,k):
    # creating a list of n element using list comph...
    l = [int(input()) for i in range(n)]
    return BinarySearch(l,k)


if __name__ == '__main__':
    n = int(input("Enter the value of n : "))
    k = int(input("Enter the value of k : "))
    CreateList(n,k)
