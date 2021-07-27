
def ParenthesisChecker(str):
    stack = []
 
   
    for char in str:
        if char in ["(", "{", "["]:
 
           
            stack.append(char)
        else:
 
           
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
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

