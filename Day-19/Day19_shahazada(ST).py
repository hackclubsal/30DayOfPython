if __name__ =='__main__':
    n=int(input("Enter size of list:- "))
    listint=[]
    print("Enter element of listint")
    dictionary={}
    ans=-1
    for i in range(n):
        ele=int(input())
        listint.append(ele)
        dictionary[ele]=0
        
    for i in listint:
        dictionary[i]+=1
    
    for  i in listint:
        if(dictionary[i]==2):
            ans=i
            
    print("{} repeates {} times".format(ans,dictionary[ans]))    
    for i in range(n):
        if(listint[i]==ans):
            listint.pop(i)
            break
        
    print("repeated {} is removed from listint {}".format(ans,listint))    
