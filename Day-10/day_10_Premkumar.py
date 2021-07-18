def sumOfNum(n):
  """ 
  This function takes integer n as a parameter and 
  returns the sum of n natural numbers 
  Example:- 
    n = 5
    returns 15
  """
  res = n*(n+1)/2
  return res 

if __name__ == "__main__":
  a = int(input("Enter a number \n"))
  print('Sum of the n natural numbers is :- {}'.format(sumOfNum(a)))
