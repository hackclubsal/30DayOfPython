""""Day 17: Implement a Queue in Python. Also perform Enqueue and Dequeue Operations."""

if __name__ == '__main__':
    queue = []
    while True:
        num = int(input("Enter the Value :\n\t 1) enqueue 2) dequque 3) Quit\n\t"))

        # for enqueuq
        if num ==1:
            data = int(input("\tEnter the value : "))
            op = queue.append(data)
            print('Queuq looks like : ',queue)

        # for dequeue
        elif num==2:
            if len(queue)>0:
                queue.pop(0)
                print('Queuq looks like : ', queue)
            else:
                print('Queue is empty.')

        #for quit
        elif num==3:
            print('Final queuq : ',queue,'\nThank you ...')
        
        # for exception
        else:
            print('Please provide valid input.')
