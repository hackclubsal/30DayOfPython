# Day-16 Question for the day-16 is --->

# -> Question: Implement a Stack in Python. Also perform Push and Pop Operations.

# -> Input: 
# push(3)
# push(7)
# push(4)
# pop()
# push(8)

# -> Output: 
# 3, 7, 8

# Hint: 
# You can implement Stack using python list and also perform stack operations using list's two methods, find out that methods.


s = []

while (1):
    print('1. Push 2. Pop 3. Print 4. Exit ')
    n = int(input('Enter number : '))
    if (n == 1):
        x = int(input('Enter number you want to push : '))
        s.append(x)
    elif (n == 2):
        try:
            print("Popped element is : ",s.pop())
        except:
            print('No element in list!')
    elif (n == 3):
        print(s)
    elif (n == 4):
        break
    else:
        print('Enter valid number!')
    

