#day23_Challenge

n = [1,2,3,4,5,6]

def cyclic(n):
    n.insert(0, 0)
    n.insert(0, 0)

    n[0] = n.pop()
    n[1] = n.pop()
    return n

print(cyclic(n))
