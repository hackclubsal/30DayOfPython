def acuratelcp(string1,string2):
    alcp=""
    i=0
    while i<len(string1) and i<len(string2):
        if string2[i]!=string1[i]:
            break
        alcp+=string1[i]
        i+=1
    return alcp    


def findlcp(stringList):
    lcp=stringList[0]
    
    for string in stringList:
        lcp=acuratelcp(lcp,string)
    
    return lcp    


if __name__ == '__main__':
    stringList=input("Enter the string:- ").split()
    
    lcp=findlcp(stringList)
    print("\n{} is longest common prefix in {}".format(lcp,stringList))
