class ascii:
    def __init__(self,char):
        self.char = char

    def find_ascii(self):
        if len(self.char) == 1:
            result = ord(self.char)
            binary = bin(int(result))[2:]
            print('ASCII Code of character {} is {} and Binary Code is {}'.format(self.char, result,binary))
        else:
            print('Length of character much be 1')

char = input("Enter the character: ")
obj = ascii(char)
obj.find_ascii()
