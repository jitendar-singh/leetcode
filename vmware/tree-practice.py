'''
PRE     INORDER     POST
val     left        left
left    val         right
right   right       val
'''
class Node:

    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key
    
def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)

print("INORDER TRAVERSAL")
printInorder(root)
print("POSTORDER TRAVERSAL")
printPostorder(root)
print("PREORDER TRAVERSAL")
printPreorder(root)