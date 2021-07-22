#Day22_Challenge

class MainNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def Inorder(root):
 
    if root:
        Inorder(root.left)

        print(root.data),
 
        Inorder(root.right)
 
root = MainNode(10)
root.left = MainNode(7)
root.right = MainNode(8)

Inorder(root)
