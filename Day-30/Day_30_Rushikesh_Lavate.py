""" Write a program to print lower triangle matrix. """
class matrix():
    def __init__(self):
        self.row = int(input("Enter row size : "))
        self.col = int(input("Enter column size : "))

    def lowermatrix(self):
        data = [int(input(f"Enter values of element {i+1} : ")) for i in range(self.row*self.col)]
        d = [data[i:i+self.col] for i in range(0,len(data),self.col)]
        print(d)
        for i in range(len(d)):
            for j in range(len(d[i])):
                if i < j:
                    d[i][j]=0
        print(d)

if __name__ == '__main__':
    obj = matrix()
    obj.lowermatrix()
