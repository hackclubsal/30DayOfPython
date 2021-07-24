#Day-24_Hackclubsal_30DayOfPython_Solution
# Python program to validate an Email

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):

 if(re.match(regex, email)):
    print("Valid Email !!")
 else:
    print("Invalid Email !!")
    
email = input("Enter Email :")
check(email)

