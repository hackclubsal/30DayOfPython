class digit:
    def __init__(self,num):
        self.num = num

    def find_digits(self):
        l = len(str(self.num))
        if (l%2)!=0:
            print("Length of number is odd.")
            last_dig = self.num % 10
            mid_dig = int(str(self.num)[int(l/2)])
            print("\tLast digit is : {}\n\tMiddle digit is :{}".format(last_dig,mid_dig))
        else:
            last_dig = self.num % 10
            print('Length of number is Even.')
            print("\tLast digit is : {}\n\tMiddle digit is :-1".format(last_dig))

num = int(input('Enter the number : '))
obj = digit(num)
obj.find_digits()
