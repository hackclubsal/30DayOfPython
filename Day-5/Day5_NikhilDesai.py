month_days = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31,
              "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}


def check_days(month_number):

    """

    This function returns the number of days in a month as user wants to know.

    """

    for key, value in month_days.items():
        if key == month_number:
            return value


if __name__ == "__main__":
    month = input("Enter a Month Number: ")
    result = check_days(month)
    print(f'This Month has {result} Days')
