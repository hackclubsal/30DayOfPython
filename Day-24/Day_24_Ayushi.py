# Day-24 Question for the day-24 is --->

# -> Question:  Write a program that validates email address with the help of regular expressions

# -> Input: 
# Email= abs@gmail.com

# -> Output:-
# Valid Email!

# -> Input:-
# Email = g33n.com

# -> Output:- 
# Invalid Email!

import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
      
if __name__ == '__main__' :   
    email = input() 
    check(email)   