class Months:

  def __init__(self,n):

    self.n=n

  

  def print_days(self):

    if (self.n==4 or self.n==6 or self.n==7 or self.n==11):

      print("30")

    elif (self.n==1 or self.n==3 or self.n==5 or self.n==8 or self.n==9 or self.n==10 or self.n==12):

      print("31")

    elif (self.n==2):

      print("28")

    else:

      print("Invalid month number")

    

n = int(input("Enter month number:"))

m = Months(n)

m.print_days()
