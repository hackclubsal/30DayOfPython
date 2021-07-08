def sumOfEven(a, b):
  """
  This function takes the parameter range i.e. [a, b]
  and returns the sum of the even numbers 
  Example :-
    if [a, b] = [0, 10]
    then this fuction returns 20
  """
  res = 0
  for num in range(a+1, b):
    if num % 2 == 0:
      res += num
  return res

if __name__ == "__main__":
  n, m = (int(i) for i in input("Enter a space seperated two integers \n").split())
  print("The sum of the even numbers in the given range {} is {}".format([n, m], sumOfEven(n, m)))