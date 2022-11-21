# Time complexity: O(n)
# Space complexity: O(h)

class Tree:
  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

  def insert(self, data):
    if self.data is None:
      self.data = data
    else:
      if data < self.data:
        if self.right is None:
          self.right = Tree(data)
        else:
          self.right.insert(data)
      elif data > self.data:
        if self.left is None:
          self.left = Tree(data)
        else:
          self.left.insert(data)

def dfsPreorder(root):
  if root is None:
    return
  print(root.data)
  dfsPreorder(root.left)
  dfsPreorder(root.right)

def dfsInorder(root):
  if root is None:
    return
  dfsInorder(root.left)
  print(root.data)
  dfsInorder(root.right)

def dfsPostorder(root):
  if root is None:
    return
  dfsPostorder(root.left)
  dfsPostorder(root.right)
  print(root.data)
  


if __name__ == "__main__":
  root = Tree(4)
  root.insert(6)
  root.insert(3)
  root.insert(5)
  root.insert(7)
  root.insert(1)
  root.insert(2)
  
  dfsPreorder(root)
          
