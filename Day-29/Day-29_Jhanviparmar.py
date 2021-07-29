#day29
def longestCommonPrefix(x):
    size = len(x)
    if (size == 0):
        return 
    if (size == 1):
        return x[0]
    x.sort()
    res = ""
    for i in range(len(x[0])):
        if x[0][i] == x[-1][i]:
            res += x[0][i]
        else:
            break
    return res
input = ["apple", "ape", "april"]
print(longestCommonPrefix(input))
