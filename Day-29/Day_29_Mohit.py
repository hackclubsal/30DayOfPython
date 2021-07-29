# Given a set of strings, find the longest common prefix.
arr = []
n = int(input("enter the length of array : "))
for i in range(0, n):
    ele = input("Enter : ")
    arr.append(ele)
print(arr)
if not arr:
    print("Longest common prefix:", "")
elif len(arr) == 1:
    print("Longest common prefix:", arr[0])
else:
    arr.sort()
    result = ""
    for i in range(len(arr[0])):
        if arr[0][i] == arr[-1][i]:
            result += arr[0][i]
        else:
            break
    print("Longest common prefix:", result)
