class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())



# test tree

if __name__=='__main__':
    rtele=input("Enter root element of tree:- ")
    
    Tree = BinaryTree(rtele)
    lft=True
    rgt=False
    while(1):
        choice=int(input("Want to insert more element enter 1 other wise 0:- "))
        if(not choice):
            break
        opcode=input("operation code for 'insrt' for insert and 'inordr' for inorder:- ")
        if(opcode=='insrt'):
            
            ele=input("Enter element for insert into tree:- ")
            if(lft):
                Tree.insertLeft(ele)
                rgt=True
                lft=False
            elif(rgt):
                Tree.insertRight(ele)
                rgt=False
                lft=True
        elif(opcode=='inordr'):
            printTree(Tree)
    
