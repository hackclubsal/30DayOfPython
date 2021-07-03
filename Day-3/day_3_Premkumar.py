def main(a):
  if a%10 == 0 and a%20 ==0:
    return True
  else:
    return False
if __name__ == "__main__":
  a = float(input("Enter a valid number here \n"))
  if main(a):
    print("Yes the given number {} is divisible by 10 and 20".format(a))
  else:
    print("No the given number {} is not divisible by 10 and 20".format(a))
