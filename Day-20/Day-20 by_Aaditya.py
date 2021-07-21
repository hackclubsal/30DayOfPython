#day20_challenge
st = input("Enter a string: ")
print(st)
st = st.split()
for i in range(0,len(st)):
    result = st[i].capitalize()
    print(result, end=" ")
