# Day-4

stars = int(input("Enter the row to display:"))


def draw(stars):
    starCount = 0
    for i in range(0, stars+1):
        for j in range(0, i):
            print("*", end='')
            starCount += 1
        print("")
    print(starCount)


draw(stars)
