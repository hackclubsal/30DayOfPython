def main(num):
  """
  This function takes numbers as input parameter and returns
  last digit and mid digit of the number
  Example :-
    num = 25475
    returns (5, 4)
  """
  last = num[-1]
  if len(num)%2 == 0:
    mid = -1
  else:
    mid = num[len(num)//2]
  return last, mid

if __name__ == "__main__":
  num = input("Enter a valid number \n")
  last, mid = main(num)
  print("Last and middle digits of the number are : {}, {}".format(last, mid))
