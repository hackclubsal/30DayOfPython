"""WAP that takes a string as an input and convert it's all first latter of words into Uppercase."""

"""
# method 1:
def convert():
    return ' '.join([i.title() for i in input("Enter the string : ").split()])
"""

# method 2:
def convert():
    try:
        str = input("Enter the string : ").split()
        if len(str) > 0:
            result = ' '.join([i.title() for i in str])
            return result
        else:
            return -1
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    print(convert())
