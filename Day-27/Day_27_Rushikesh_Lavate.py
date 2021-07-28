"""Question: Parenthesis Checker """
def ParenthesisCheck(exp='{([])}'):
    stack = []
    for char in exp:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            cur_char = stack.pop()
            if cur_char == '(':
                if char != ")":
                    return False
            if cur_char == '[':
                if char != "]":
                    return False
            if cur_char == '{':
                if char != "}":
                    return False

    if stack:
        return False
    return True

exp = input("Enter the expression string : ")
print(ParenthesisCheck(exp))
