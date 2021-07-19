# Remove Duplicates from the given array and also print duplicate number.
'''def checkIfDuplicates(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


def main():

    listOfElems = []
    dupli = []
    n = int(input("Enter the Elements Range : "))
    for i in range(0, n):
        ele = int(input("Element : "))
        if i not in listOfElems:
            listOfElems.append(ele)
        else:
            dupli.append(ele)

    result = checkIfDuplicates(listOfElems)
    if result:
        print('Yes, list contains duplicates')
        print(dupli, "are the duplicates")
    else:
        print('No duplicates found in list')
        print(listOfElems, " are the non-duplicates")


if __name__ == '__main__':
    main()

'''

# Day 19: Remove Duplicates from the given array and also print duplicate number.


def remove_duplicates(n):

    lst = [int(input()) for i in range(n)]
    unique = []
    dupli = []
    for i in lst:
        if i not in unique:
            unique.append(i)
        else:
            dupli.append(i)

    print('Original list : ', lst)
    print('List without duplicates : ', unique)

    if len(dupli) >= 1:
        print('Duplicate elements : ', list(set(dupli)))
    else:
        print('There is no duplicate present.')


if __name__ == '__main__':
    num = int(input("Enter length of array : "))
    remove_duplicates(num)
