


month = {
        1: "31", 
        2: "28",
        3: "31",
        4: "30",
        5: "31",
        6: "30",
        7: "31",
        8: "31",
        9: "30",
        10: "31",
        11: "30",
        12: "31"
    }
n = int(input("Enter month number : "))
if( n > 12 or n < 1):
    print("Invalid month number!")
else:
    print(month[n]) 


    


