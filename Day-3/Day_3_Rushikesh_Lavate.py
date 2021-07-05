class divisibilty:

  def __init__(self,num):

    self.num = num



  def display(self):

    if ((self.num%10==0) and (self.num%20==0)):

      print(self.num,"is dividible by both 10 and 20")

    else:

      print(self.num,"is not dividible by 10 and 20")

a = int(input("Enter a number: "))

x = divisibilty(a)

x.display()
