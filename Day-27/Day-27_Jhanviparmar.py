#day27
def check(string,n):
    ans = True
    s = []
    for i in string:
        if i=='(' or i=="{" or i=="[" :
            s.append(i)
        else:
            if len(s)>0:
                temp = s[len(s)-1]
                s.pop()
                if i=="(" and temp!=")" :
                    ans = False
                    break
                if i=="{" and temp!="}" :
                    ans = False
                    break
                if i=="[" and temp!="]" :
                    ans = False
                    break
            else:
                ans = False
    if len(s)>0:
        ans=False
    if ans:
        print("True")
    else:
        print("False")
string = "(){}[()]"
n = len(string)
check(string,n)
