# Day-9 Question for the day-9 is --->

# -> Question: Write a program that returns the last digit in a number.

# -> Input: Take number as input from the user and store it in a variable.

# -> Output: print the last digit of the number.

# -> Example
# Input: 25475
# Output: 5

# Advance (not for beginners):
# If the length of the number is odd then find the middle digit  of the number otherwise return -1

# Input: 25457
# Output: 4

def main(num):
  last = num[-1]
  if len(num)%2 == 0:
    mid = -1
  else:
    mid = num[len(num)//2]
  return last, mid

if __name__ == "__main__":
  num = input()
  last, mid = main(num)
  print(f"Last and middle digits of the number are : {last}, {mid}")
