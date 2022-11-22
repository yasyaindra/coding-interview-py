from binarytree import Node

root = Node(6)
root.left = Node(8)
root.right = Node(13)
root.right.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.left.left = Node(7)
root.left.left.right = Node(3)

def reverseBinary(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    reverseBinary(tree.left)
    reverseBinary(tree.right)

reverseBinary(root)

print(root)