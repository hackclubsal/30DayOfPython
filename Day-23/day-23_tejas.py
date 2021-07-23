n = [1, 54, 32, 12]


def cyclical(n):
    n.insert(0, 0)
    n.insert(0, 0)

    n[0] = n.pop()
    n[1] = n.pop()
    return n


print(cyclical(n))
