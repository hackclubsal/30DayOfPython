"""
    Question: Two Sum: Given an array of integers nums and an integer target, 
    :return:
        indices of the two numbers such that they add up to target
"""
import numpy
class find_position:
    def __init__(self):
        numpy.random.seed(20)
        self.arr = numpy.random.randint(1,10,numpy.random.randint(6,8))
        self.num = int(input("Enter target wants : "))

    def get_position(self):
        print(self.arr)
        l = list(self.arr)
        for i in range(len(l)):
            for j in range(i):
                if (l[i] + l[j]) == self.num:
                    return (j,i)

if __name__ == '__main__':
    object = find_position()
    pos = object.get_position()
    print(pos)
