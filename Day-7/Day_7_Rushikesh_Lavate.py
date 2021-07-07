class natural_num:
    def __init__(self,n,m):
        self.n = n
        self.m = m

    def find_nat_num(self):
        if (self.n>0 and self.m>0) and (self.n+1 < self.m):
            for i in range(self.n+1,self.m):
                print(i,end=',')
        else:
            print("Value of both 'n' and 'm' must be greater than 0 and 'n' is less than 'm'")

n = int(input("Start : "))
m = int(input("End : "))
obj = natural_num(n,m)
obj.find_nat_num()
