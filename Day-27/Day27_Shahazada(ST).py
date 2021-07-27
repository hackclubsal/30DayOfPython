def checkBalance(string):
    stack=[]
    openpbb=['(','{','[']
    for pbb in string:
        if pbb in openpbb:
            stack.append(pbb)
        
        else:
            if not stack:
                return False
            
            currPbb=stack.pop()
            
            if currPbb == '(' and pbb != ')':
                return False
            
            elif currPbb == '{' and pbb != '}':
                return False
            
            elif currPbb == '[' and pbb != ']':
                return False
                
    if stack:
        return False
    return True    


if __name__ == '__main__':
    string=input("Enter string of parentheses '()' , braces '{}' and bracket '[]' :- ")
    
    if checkBalance(string):
        print(" Balance ")
    else:
        print(" Imbalance ")
    
