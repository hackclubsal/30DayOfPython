class day_1:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Hello guys,\n\tMy name is {},\n\tThank you for giving me an opportunity to contribute to the open-source community.".format(self.name))

name = input("Enter your name : ")
obj = day_1(name='Rushikesh Lavate')
obj.show()
