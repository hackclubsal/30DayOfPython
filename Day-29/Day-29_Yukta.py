lst = [ ]
n = int(input("Enter number of elements : "))
def lcp(lst, n):
   if(n == 0):
       return " "
   if(n == 1):
        return(lst[0])
   lst.sort()
   min_str = min(len(lst[0]), len(lst[n-1]))
   i = 0
   while(i < min_str and lst[0][i] == lst[n-1][i]):
       i = i + 1
   prefix = lst[0][0: i]
   return prefix
   




 
for i in range(0, n):
    ele = input()
    lst.append(ele)
     
print(lst)
print("Longest common prefix : ", lcp(lst,n))