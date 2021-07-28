def areBracketsBalanced(expr):
	stack = []

	
	for char in expr:
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


expr = input("Enter a string:")

	
if areBracketsBalanced(expr):
	print("True")
else:
	print("False")
