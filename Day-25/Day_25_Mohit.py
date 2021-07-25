# our two sum function which will return all pairs in the array that sum up to S
def twosum(arr, target):
    dict = {}
    results = []
    for i in arr:
        if (target - i) in dict:
            if dict[target - i]:
                continue
            results.append([i, target - i])
            dict[target - i] = True
        else:
            dict[i] = False
    return results


lst = []
n = int(input("Enter the Elements Range in array : "))
for i in range(0, n):
    ele = int(input("Element : "))
    lst.append(ele)
print(lst, " are the elemnts.")

k = int(input("Enter the Number for target : "))

print(twosum(lst, k))
