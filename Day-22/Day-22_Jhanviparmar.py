class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def Inorder(root):
 
    if root:
        Inorder(root.left)

        print(root.data),
 
        Inorder(root.right)
 
 
root = Node(10)
root.left = Node(7)
root.right = Node(8)

Inorder(root)
 
