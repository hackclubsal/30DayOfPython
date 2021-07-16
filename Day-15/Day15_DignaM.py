# Day-15_Hackclubsal_30DayOfPython_Solution
#  Quick Sort

n=int(input("Enter size of array :"))
a=[]
for i in range(0,n):
    x=int(input("Enter element"))
    a.append(x)
print("Before sorting:",a)

def part(start, end, a):
    pivot_index = start
    pivot = a[pivot_index]

    while start < end:
        while start < len(a) and a[start] <= pivot:
            start += 1

        while a[end] > pivot:
            end -= 1

        if (start < end):
            a[start], a[end] = a[end], a[start]
    a[end], a[pivot_index] = a[pivot_index], a[end]
    return end

def quick_sort(start, end, a):
    if (start < end):
        p = part(start, end, a)
        quick_sort(start, p - 1, a)
        quick_sort(p + 1, end, a)

quick_sort(0, len(a) - 1, a)

print(f'Sorted a: {a}')
