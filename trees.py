class Node:
    def __init__(self, key):
        self.value = key
        self.right = None
        self.left = None

def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

root = Node(5)
root.left = Node(2)
root.right = Node(3)

root.left.right = Node(1)
root.left.left = Node(-1)
root.right.right = Node(8)

print("Preorder: ")
preorder(root)
print()
print("Inorder: ")
inorder(root)
print()
print("Postorder: ")
postorder(root)