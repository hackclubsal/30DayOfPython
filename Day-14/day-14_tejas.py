import random


def bubblesort():
    m = []

    n = int(input("Enter the number of elements: "))

    for i in range(n):
        m.append(random.randint(1, 100))

    print(m)
    for j in range(len(m)):
        for i in range(len(m)-1):
            if m[i] > m[i+1]:
                m[i], m[i+1] = m[i+1], m[i]
            else:
                m[i], m[i+1] = m[i], m[i+1]

    print("Sorted array: ")
    print(m)


bubblesort()
