def stack():
    stk = []
    """ Use append method for pushing data into stack"""
    while True:
        print('Choose option :\n\t1. Push 2. Pop 3. Quit ')
        choice = int(input('Enter choice : '))
        if (choice == 1):
            data = int(input('Enter data you want to push : '))
            stk.append(data)
            print(stk)
        elif (choice == 2):
            if len(stk)>0:
                print("Popped element is",stk.pop())
                print(stk)
            else:
                print('No element in list')
                print(stk)
        elif (choice == 4):
            print('Final stack : ',stk)
            break
        else:
            print('Enter valid number')
    return stk

if __name__ == '__main__':
    print(stack())
