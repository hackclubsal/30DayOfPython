def linearSearch(n,k):
    l = []
    # creating a list of n element using list comph...
    [l.append(int(input())) for i in range(n)]
    print(l)
    ind = -1

    # find our key element is present or not
    for j in l:
        if k==j:
            ind = l.index(k)
    print(ind)

if __name__ == '__main__':
    n = int(input("Enter the value of n : "))
    k = int(input("Enter the value of k : "))
    linearSearch(n,k)
