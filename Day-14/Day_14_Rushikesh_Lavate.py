def BubbleSort(n):
    l = []
    # creating a list of n element using list comph...
    [l.append(int(input())) for i in range(n)]
    print(l)

    # apply Bubble sort logic
    for i in range(n):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j] , l[j+1] = l[j+1],l[j]
    print(l)

if __name__ == '__main__':
    n = int(input("Enter the value of n : "))
    BubbleSort(n)
