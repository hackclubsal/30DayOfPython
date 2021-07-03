def check_number(num):
    '''

    This function Checks whether a number is divisible by 10 and 20

    '''

    if num > 0:
        if all([num % 10 == 0, num % 20 == 0]):
            return True


if __name__ == "__main__":
    number = int(input("Enter a Number To Check: "))
    result = check_number(number)
    if result:
        print(f'{number} is divisible by both 10 & 20')
    else:
        print("{} Cannot divisible by 10 & 20".format(number))
