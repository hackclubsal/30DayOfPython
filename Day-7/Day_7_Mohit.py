# Write a program to print all the natural numbers between n and m (Where n and m are user input and n>0, m>0)

i1 = int(input("Enter the first Number :"))
i2 = int(input("Enter the Second Number :"))

for i3 in range(i1, i2):
    if i3 > i1:
        print(i3)
