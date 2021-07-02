def get_cuberoot(num):

    '''
    This Program returns cuberoot of user input
    '''

    if num > 0:
        return round(num ** (1/3), 2)
    else:
        return round(-(-num) ** (1/3), 2)

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f'\n CubeRoot of given {number} is {get_cuberoot(number)}')
