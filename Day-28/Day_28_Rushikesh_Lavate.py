import numpy as np
class find_num:
    def __init__(self):
        self.row = int(input("Enter the rows size : "))
        self.col = int(input("Enter the columns size : "))

    def creaate_array(self):
        result = False
        if ((self.row >= 1) and (self.col >= 1)):
            if (self.row == 1) and (self.col == 1):
                arr = np.random.randint(1,99)
                print([arr])
                num = int(input("Enter number want to find : "))
                if arr==num:
                    result = True

            elif (self.row==1) and (self.col>1):
                arr = np.random.randint(1,99,self.col)
                print(arr)
                num = int(input("Enter number want to find : "))
                arr = list(arr)
                for i in arr:
                    if int(i)==num:
                        result = True

            else:
                arr = list(np.random.randint(1,99,size=(self.row,self.col)))
                print(arr)
                num = int(input("Enter number want to find : "))
                for i in arr:
                    for j in i:
                        if int(j)==num:
                            result = True
        else:
            return "Values must be greater than zero !"

        if result:
            return True
        else:
            return False

if __name__ == '__main__':
    obj = find_num()
    print(obj.creaate_array())
