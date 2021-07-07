value = []


def natural_numbers(num_1, num_2):

    """
    This function returns natural numbers between user inputs

    :param num_1: 6
    :param num_2: 12
    :return: [7, 8, 9, 10, 11]
    """

    if (num_1 > 0) & (num_2 > 0):
        for i in range(1, num_2):
            num = num_1 + i
            value.append(num)

            if num == num_2 - 1:
                break

        return value

    else:
        for i in range(-1, num_2, -1):
            num = num_1 + i
            value.append(num)

            if num == num_2 + 1:
                break

        return value


if __name__ == "__main__":
    num1 = int(input("Enter a 1st Number: "))
    num2 = int(input("Enter a 2nd Number: "))
    numbers = natural_numbers(num1, num2)
    print(f'Natural Numbers between {num1} and {num2} are: {numbers}')
