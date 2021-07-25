# Day-22 Question for the day-22 is --->

# -> Question: Implement a Binary Tree Data Structure in Python

# -> Input: 
# Node(10)
# Node(7)
# Node(8)

# -> Output:-
# 7 10 8 (using Inorder traversal)


class MainNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def Inorder(root):
 
    if root:
        Inorder(root.left)

        print(root.data, end=" "),
 
        Inorder(root.right)
 
root = MainNode(10)
root.left = MainNode(7)
root.right = MainNode(8)

Inorder(root)
