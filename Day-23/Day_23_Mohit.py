
def solution(A, K):
    old = A
    new = [0]*len(A)
    for i in range(K):
        new[0] = old[-1]
        new[1:] = old[:-1]
        old = new.copy()  # This was the problematic line
    return new


n = int(input("Enter the Elements Range : "))
k = int(input("enter number of Rotation : "))
arr = []
for i in range(0, n):
    ele = int(input("Element : "))
    arr.append(ele)
print(arr, " is the first inserted Array.")
print(solution(arr, k), "is the rotated Array.")
