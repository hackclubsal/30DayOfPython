# Day-17 Question for the day-17 is --->

# -> Question: Implement a Queue in Python. Also perform Enqueue and Dequeue Operations.

# -> Input: 
# Enqueue(9)
# Enqueue(7)
# Dequeue()
# Enqueue (8)

# -> Output: 
# 7, 8

# Hint: 
# Use Python List and it's append and pop methods.


q = []

while (1):
    print('1. Enqueue 2. Dequeue 3. Print 4. Exit ')
    n = int(input('Enter number : '))
    if (n == 1):
        x = int(input('Enter number you want to Enqueue : '))
        q.append(x)
    elif (n == 2):
        try:
            print("Dequeued element is : ",q.pop(0))
        except:
            print('No element in list!')
    elif (n == 3):
        print(q)
    elif (n == 4):
        break
    else:
        print('Enter valid number!')
