"""Day 19: Remove Duplicates from the given array and also print duplicate number."""
def remove_duplicates(n):

    lst = [int(input()) for i in range(n)]
    unique = []
    dupli = []
    for i in lst:
        if i not in unique:
            unique.append(i)
        else:
            dupli.append(i)

    print('Original list : ',lst)
    print('List without duplicates : ',unique)

    if len(dupli)>=1:
        print('Duplicate elements : ', list(set(dupli)))
    else:
        print('There is no duplicate present.')

if __name__ == '__main__':
    num = int(input("Enter length of array : "))
    remove_duplicates(num)
