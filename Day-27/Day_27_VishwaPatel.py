def areBracketsBalanced(expr):
	stack = []

	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
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


# Driver Code
if __name__ == "__main__":
	expr = input('Enter expression')

	if areBracketsBalanced(expr):
		print(True)
	else:
		print(False)


