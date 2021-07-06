def ascii_value(char):
    """

    This function return an ASCII value of given character

    """
    return ord(char)


def binary_value(num):
    """

    This function returns Binary value of given ASCII value

    """
    return bin(num).replace("0b"," ")


if __name__ == "__main__":
    str_value = input("Enter a character: ")
    result = ascii_value(str_value)
    print("ASCII value of given Character is: {}".format(result))
    bin_value = binary_value(result)
    print(f'Binary value of given Character is: {bin_value}')
