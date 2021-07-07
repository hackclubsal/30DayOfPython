#day4_challenge

st = int(input("Enter the row to display:"))
def draw(st):
    starCount = 0
    
    for i in range(0, st+1):
        for j in range(0, i):
            print("*", end='')
            starCount += 1
        print("")
    print(starCount)

draw(st)
