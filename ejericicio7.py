from avltree import*

def height(AVLTree):
  if AVLTree.root != None:
    return heightR(AVLTree.root)

def heightR(node):
  if node.bf > 0:
    return heightR(node.leftnode) + 1
  elif node.bf < 0:
    return heightR(node.rightnode) + 1
  elif node.leftnode != None and node.rightnode != None:
    return heightR(node.leftnode) + 1
  else:
    return 0

def TwoTrees(A, B, X):
  if A.root == None and B.root == None:
    newnode = AVLNode()
    newnode.key = X
    newnode.bf = 0
    A.root = newnode
    return A
  elif B.root != None and A.root == None:
    insert(B, None, X)
    return B
  elif A.root != None and B.root == None:
    insert(A, None, X)
    return A
  else:
    newnode = AVLNode()
    newnode.key = X
    newnode.bf = 0
    ha = height(A)
    hb = height(B)
    if ha > hb:
      cur = A.root
      for lvl in range(1, ha - hb):
        cur = cur.rightnode
      newnode.leftnode = cur.rightnode
      newnode.rightnode = B.root
      newnode.parent = cur
      cur.rightnode = newnode
      return A
    elif ha < hb:
      cur = B.root
      for lvl in range(1, hb - ha):
        cur = cur.leftnode
      newnode.rightnode = cur.leftnode
      newnode.leftnode = A.root
      newnode.parent = cur
      cur.leftnode = newnode
      return B
    else:
      newnode.leftnode = A.root
      newnode.rightnode = B.root
      A.root.parent = newnode
      B.root.parent = newnode
      A.root = newnode
      return A