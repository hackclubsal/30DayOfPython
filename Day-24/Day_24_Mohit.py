# Write a program that validates email address with the help of regular expressions
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):

    if(re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")


email = "mohit@gmail.com"
check(email)
