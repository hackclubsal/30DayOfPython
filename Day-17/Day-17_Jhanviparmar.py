#day17
queue = []
while (1):
    print('1 for Enqueue, 2 for Dequeue, 3 for Print, 4 for Exit ')
    n = int(input('Enter number according to operation: '))
    if (n == 1):
        x = int(input('Enter number you want to enqueue: '))
        queue.append(x)
    elif (n == 2):
        try:
            print("Dequeued element is: ",queue.pop(0))
        except:
            print('No element in queue')
    elif (n == 3):
        print(queue)
    elif (n == 4):
        break
    else:
        print('Enter a natural number less than 3')
