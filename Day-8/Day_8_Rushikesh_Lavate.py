class even_sum:
    def __init__(self,n,m):
        self.n = n
        self.m = m
    def find_even_sum(self):
        if (self.n < self.m):
            sum = 0
            for i in range(self.n,self.m):
                if i%2==0:
                    sum = sum+i
            print(sum)
        else:
            print('Starting number is greater then ending.')
n = int(input('Enter starting number :'))
m = int(input('Enter ending number :'))
obj = even_sum(n,m)
obj.find_even_sum()
