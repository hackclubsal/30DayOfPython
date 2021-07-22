#Day-22_Hackclubsal_30DayOfPython_Solution
#Program to Implement a Binary Tree Data Structure in Python


class newNode():
    def __init__(self,info):
        self.k = info
        self.l = None
        self.r = None

def inorder(tmp):
    if (not tmp):
        return
    inorder(tmp.l)
    print(tmp.k,end =  " ")
    inorder(tmp.r)

def insert(tmp,k):
    if(not tmp):
        root_node = newNode(k)
        return

    q = []
    q.append(tmp)

    while(len(q)):
        tmp = q[0]
        q.pop(0)

        if (not tmp.l):
            tmp.l = newNode(k)
            break
        else:
            q.append(tmp.l)

        if (not tmp.r):
            tmp.r = newNode(k)
            break
        else:
            q.append(tmp.r)

if __name__ == '__main__' :
    root_node = newNode(10)
    root_node.l = newNode(7)
    root_node.r = newNode(8)

    print("Inorder traversal of given binary tree is : ", end=" ")
    inorder(root_node)