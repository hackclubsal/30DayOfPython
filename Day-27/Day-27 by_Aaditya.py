#Day27_Challenge

def ParenthesisChecker(str):
    stack = []
 
    for i in str:
        if i in ["(", "{", "["]:
             stack.append(i)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if i != ")":
                    return False
            if current_char == '{':
                if i != "}":
                    return False
            if current_char == '[':
                if i != "]":
                    return False
 
    if stack:
        return False
    return True
 
 
if __name__ == "__main__":

    str = input("Enter string: ")
    
    if ParenthesisChecker(str):
        print("TRUE")
    else:
        print("FALSE")
