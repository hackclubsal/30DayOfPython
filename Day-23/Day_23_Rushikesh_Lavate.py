"""Write a program to cyclically rotate an array by two"""
import numpy
def create_arr():
    numpy.random.seed(20)
    return numpy.random.randint(1, 10,numpy.random.randint(4,7))

def shift(arr):
    arr = list(arr)
    print("Before roration : ",arr)
    for i in range(2):
        arr.insert(0,arr.pop())
    print("After roration : ",arr)

if __name__ == '__main__':
    arr=create_arr()
    shift(arr)
