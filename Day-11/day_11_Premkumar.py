def fib(n):
  """
  This function takes n as an integer and returns 
  nth fibonacci number 
  Example :-
    n = 9
    returns 34
  """
  if n == 1:
    return 0
  if n == 2:
    return 1
  f1, f2 = 0, 1
  for i in range(1, n):
    f1, f2 = f2, f1+f2
  return f2

if __name__ == "__main__":
  n = int(input("Enter a positive integer \n"))
  print("{}th fibonaci number is {}".format(n, fib(n)))