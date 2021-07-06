list = []


def decTobinary(Number):
    while Number > 0:
        list.append(Number % 2)
        Number = Number//2


character = input("Enter the character : ")
print("ASCII of", character, "=", ord(character))
decTobinary(ord(character))
print("Binary :")
list.reverse()
for i in list:
    print(i, end='')
