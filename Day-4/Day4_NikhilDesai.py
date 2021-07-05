count = 0


def get_pyramid(num):

    '''

    This function returns Pyramid pattern and counts total stars in it.

    '''

    global count
    for i in range(num):
        star = ''
        for j in range(i+1):
            star += "*"
            count += 1
        print(star)
    return count


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = get_pyramid(number)
    print(f'\n Total Stars in the Pyramid are: {result}')
