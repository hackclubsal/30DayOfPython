def titleBuiltin(string):
    print(' "{}" is Original string '.format(string))
    print('title() is  inbuilt function of string,it just generate a titled string not convert original string')
    print(' "{}" is titled string '.format(string.title()))

def capitalizeBuiltin(string):
    stringsplit=string.split() #convert string to list of string
    print(stringsplit) 
    st=" ".join(i.capitalize() for i in stringsplit) #join by space each element string to make string
    print("'{}' is original string ".format(string))
    print("'{}' is titled string ".format(st))    


if __name__ =='__main__':
    string=input("Enter a String:- ")
    choice=input('Enter "title" for using inbuilt title function or enter "capitalize" for using inbuilt capitalize function  to covert titled string:- ')
    choice=choice[0].lower()
    if choice=='builtin':
        titleBuiltin(string)
    elif choice=='capitalize':
        capitalizeBuiltin(string)
    else:
        print("Wrong choice try again")

        
