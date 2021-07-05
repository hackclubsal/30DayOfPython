if __name__ == "__main__":
    def getDate(a):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        print(f"There are {days[a-1]} days in the month of {months[a-1]}")
        return 0

    a = int(input("Enter the month in integer: "))
    getDate(a)