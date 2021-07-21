#day16
stack = []
while (1):
    print('1 for Push, 2 for Pop, 3 for Print, 4 for Exit ')
    n = int(input('Enter number according to operation: '))
    if (n == 1):
        x = int(input('Enter number you want to push: '))
        stack.append(x)
    elif (n == 2):
        try:
            print("Popped element is: ",stack.pop())
        except:
            print('No element in list')
    elif (n == 3):
        print(stack)
    elif (n == 4):
        break
    else:
        print('Enter a natural number less than 3')
