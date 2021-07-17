q = []

while (1):
    print('1. Enqueue 2. Dequeue 3. Print 4. Exit ')
    n = int(input('Enter number'))
    if (n == 1):
        x = int(input('Enter number you want to insert'))
        q.append(x)
    elif (n == 2):
        try:
            print("Popped element is",q.pop(0))
        except:
            print('No element in list')
    elif (n == 3):
        print(q)
    elif (n == 4):
        break
    else:
        print('Enter valid number')
