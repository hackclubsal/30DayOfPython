value = []


def sum_of_numbers(num_1, num_2):

    """
    This function returns natural numbers between user inputs

    :param num_1: 0
    :param num_2: 10
    :return: sum([2, 4, 6, 8]) = 20
    """

    if (num_1 >= 0) & (num_2 >= 0):
        for i in range(1, num_2):
            num = num_1 + i

            if num % 2 == 0:
                value.append(num)

            if num == num_2:
                break

        return sum(value)

    else:
        for i in range(-1, num_2, -1):
            num = num_1 + i

            if num % 2 == 0:
                value.append(num)

            if num == num_2:
                break

        return sum(value)


if __name__ == "__main__":
    num1 = int(input("Enter a 1st Number: "))
    num2 = int(input("Enter a 2nd Number: "))
    numbers = sum_of_numbers(num1, num2)
    print(f'Sum of Natural Numbers between {num1} and {num2} are: {numbers}')
