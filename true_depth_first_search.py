# Time complexity: O(n)
# Space complexity: O(h)
from binarytree import Node

root = Node(4)
root.left = Node(6)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(2)

# def dfsPreorder(root):
#   if root is None:
#     return
#   print(root.value)
#   dfsPreorder(root.left)
#   dfsPreorder(root.right)


# def dfsInorder(root):
#   if root is None:
#     return
#   dfsInorder(root.left)
#   print(root.value)
#   dfsInorder(root.right)
  
# dfsInorder(root)

def dfsPostorder(root):
  if root is None:
    return
  dfsPostorder(root.left)
  dfsPostorder(root.right)
  print(root.value)

dfsPostorder(root)
          
