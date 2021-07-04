n = int(input("enter the rows you want to print: "))

def pyramid(n):
    star = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            star++
            print("* ", end="")
        print("\n")
    print(star)
    
pyramid(n)    
    
