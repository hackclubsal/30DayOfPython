def begineer(n):
    return n%10
def advance(n):
    if len(str(n))%2==0:
        return -1
    return (int(n/(10**(len(str(n))//2))))%10
n=int(input("Enter a Number: "))
print(f'The last digit of {n} is',begineer(n))
print(f'The Middle digit of {n} is',advance(n))