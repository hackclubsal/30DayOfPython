class pattern:

  def __init__(self,num):

    self.num = num

  

  def display(self):

    counter=0

    for i in range (1,self.num+1):

        print('* '*i)

        counter +=i

    print(counter)

a = int(input("Enter a number: "))

x = pattern(a)

x.display()
