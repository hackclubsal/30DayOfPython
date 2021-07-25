num = []
n = int(input("Enter size of list :"))
for i in range(0, n):
    ele = int(input())
    num.append(ele)

ans = []

target = int(input("Enter target: "))
for i in range (0,n):
	 if (num[i-1] + num[i] == target) :
		 ans.append(i-1)
		 ans.append(i)

	 else:
		 i = i+1

print(ans)

