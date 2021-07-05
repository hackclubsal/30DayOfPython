def printPattern(num):
  """ 
  In this function we take parameter num as the number of lines
  required for printing the star pattern and it will return the 
  total number of stars in the pyramid
  
  example :-
    parameter num = 3
    pyramid constructed is 
    *
    **
    ***
    total number of stars are 6
  """
  assert num >0, "Please Enter a Positive valid Number"
  symbol = "* "
  pyramid = [symbol*i for i in range(1, num+1)]
  for line in pyramid:
    print(line)
  print("Total Number of stars in the Pyramid are :- {}".format((num*(num+1))/2))

if __name__ == "__main__":
  a = int(input("Enter the number of Lines \n"))
  printPattern(a)