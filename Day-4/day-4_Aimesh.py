def printPyramid(rows):
    stars = 0
    for row in range(0, rows):
        for col in range(0, row+1):
            stars += 1
            print("* ", end="")
        print("\r")
    print(f"Number of stars = {stars}")
    return 0

rows = int(input("Enter the Number of Rows: "))
printPyramid(rows)
