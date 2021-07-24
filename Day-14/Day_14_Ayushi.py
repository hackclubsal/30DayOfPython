# Day-14 Question for the day-14 is --->

# -> Question: Perform a Bubble Sort Algorithm in a Python Program.

# -> Input: N, arr[ ]
# N- is number of elements in an array.

# -> Output: print sorted array.

# -> Example
# Input: 4, [54, 24, 34, 12]

# Output: [12, 24, 34, 54]


# -> Example

# Input: 10, [4, 3, 45, 11, 6, 86, 65, 23, 90, 55]

# Output: [3, 4, 6, 11, 23, 45, 55, 65, 86, 90]


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
