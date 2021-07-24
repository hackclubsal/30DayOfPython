"""Write a program that validates email address with the help of regular expressions"""
import re
def check_mail(mail):
    r = r'\b[A-Za-z0-9.-_]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
    if re.match(r,mail):
        print('Valid mail id')
    else:
        print('Invalid mail id')

if __name__ == '__main__':
    mail = input("Enter your mail id : ")
    check_mail(mail)
