# Day-5

month = int(input("Enter the month to find total days:"))

monthList = {
    1: "31",  # January
    2: "28",  # February
    3: "31",  # March
    4: "30",  # April
    5: "31",  # May
    6: "30",  # June
    7: "31",  # July
    8: "31",  # August
    9: "30",  # September
    10: "31",  # October
    11: "30",  # November
    12: "31"  # December
}
# print(monthList.get(1))
for i in monthList.keys():
    if month > 12 or month < 1:
        print("Invalid Month")
        break
    if i == month:
        print(monthList[i])
