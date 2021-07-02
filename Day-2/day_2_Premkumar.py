def cubeRoot(a):
  """
  This function returns the cube root of the 
  given value 'a' (assumeing a value is positive)

  eg:- 
    if a = 125 
    this function returns cube root of a
    i.e. 5
  """
  if a<0:
    return "Please try with positive number"
  cubeRootVal = a**(1/3)
  return round(cubeRootVal, 3)

if __name__ == "__main__":
  a_val = float(input("Enter a valid Number :- "))
  print(cubeRoot(a_val))