def main(a):
  """
  This function takes a integer variable in range [1, 12] and 
  prints the number of days in that month 

  Example:
    input :- 4
    output :- Number of days in month of April are 30
  """
  assert 0<a<13, "Enter Number in range [1, 12]"
  months = {1: ["January", 31], 
              2: ["February",28], 
              3: ["March", 31], 
              4: ["April", 30], 
              5: ["May", 31], 
              6: ["June", 30], 
              7: ["July", 31], 
              8: ["August", 31], 
              9: ["September", 30], 
              10: ["October", 31], 
              11: ["November", 30], 
              12: ["December",31] 
              }
  month = months[a]
  print("Number of days in the given month of {} are {}".format(month[0], month[1]))
  
if __name__ == "__main__":
  a = int(input("Enter a valid Number \n"))
  main(a)