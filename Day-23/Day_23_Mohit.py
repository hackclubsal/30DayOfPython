# Python3 program to construct tree from Array
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None



def insertLevelOrder(arr, root, i, n):

    if i < n:
        temp = newNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root

# Function to print tree nodes

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


arr = []
n = int(input("Enter the Elements Range : "))
for i in range(0, n):
    ele = int(input("Element : "))
    arr.append(ele)

print("Array : ", arr)
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)
inOrder(root)
