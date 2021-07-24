
import re

def emailvalidation(email_regex,email):
 
    if(re.match(email_regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
 
# Driver Code
if __name__ == '__main__':
    email_regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    email=input("Enter your mail address to check it is valid or not:- ")
    
    emailvalidation(email_regex,email)
    
 
    
