from algo1 import*
from linkedlist import LinkedList, add
from inversa import inversa
from myqueue import enqueue, dequeue

class AVLTree:
  root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None
  leftsize = None
  rightsize = None

def rotateLeft(Tree,avlnode):
  if avlnode.rightnode != None:
    newroot = avlnode.rightnode
    if newroot.leftnode != None:
      newroot.leftnode.parent = avlnode
      avlnode.rightnode = newroot.leftnode
    newroot.parent = avlnode.parent
    if avlnode.parent.leftnode == avlnode:
      avlnode.parent.leftnode = newroot
    else:
      avlnode.parent.rightnode = newroot
    if avlnode.parent == None:
      Tree.root = newroot
    avlnode.parent = newroot
    newroot.leftnode = avlnode
    return newroot
  return avlnode

def rotateRight(Tree, avlnode):
  if avlnode.leftnode != None:
    newroot = avlnode.leftnode
    if newroot.rightnode != None:
      avlnode.leftnode = newroot.rightnode
      newroot.rightnode.parent = avlnode
    newroot.parent = avlnode.parent
    if avlnode.parent.leftnode == avlnode:
      avlnode.parent.leftnode = newroot
    else:
      avlnode.parent.rightnode = newroot
    if avlnode.parent == None:
      Tree.root = newroot
    avlnode.parent = newroot
    newroot.rightnode = avlnode
    return newroot
  return avlnode

def calculatebalance(AVLTree):
  if AVLTree.root == None:
    return
  else:
    calculatebalanceR(AVLTree.root)
    
def calculatebalanceR(node):
  if node.leftnode == None and node.rightnode == None:
    node.leftsize = 0
    node.rightsize = 0
    node.bf = 0
    return 0
  elif node.leftnode != None and node.rightnode != None:
    node.leftsize = calculatebalanceR(node.leftnode) + 1
    node.rightsize = calculatebalanceR(node.rightnode) + 1
    node.bf = node.leftsize - node.rightsize
    if node.leftsize > node.rightsize:
      return node.leftsize
    else:
      return node.rightsize
  elif node.leftnode != None:
    node.leftsize = calculatebalanceR(node.leftnode) + 1
    node.rightsize = 0
    node.bf = node.leftsize
    return node.leftsize
  else:
    node.leftsize = 0
    node.rightsize = calculatebalanceR(node.rightnode) + 1
    node.bf = - node.rightsize
    return node.rightsize

def reBalance(AVLTree):
  calculatebalance(AVLTree)
  reBalanceR(AVLTree.root, AVLTree)
  return AVLTree

def reBalanceR(node, AVLTree):
  equilibrado = False
  if node.bf > 1:
    if node.leftnode.bf > 1 or node.leftnode.bf < -1:
      reBalanceR(node.leftnode, AVLTree)
      equilibrado = True
    if node.rightnode != None:
      if node.rightnode.bf > 1 or node.rightnode.bf < -1:
        reBalanceR(node.rightnode, AVLTree)
        equilibrado = True
    if node.leftnode.bf < 0 and equilibrado == False:
      rotateLeft(AVLTree, node.leftnode)
      rotateRight(AVLTree, node)
      balancearriba(node, AVLTree)
    elif equilibrado == False:
      rotateRight(AVLTree, node)
      balancearriba(node, AVLTree)
  elif node.bf < -1:
    if node.rightnode.bf > 1 or node.rightnode.bf < -1:
      reBalanceR(node.rightnode, AVLTree)
      equilibrado = True
    if node.leftnode != None:
      if node.leftnode.bf > 1 or node.leftnode.bf < -1:
        reBalanceR(node.leftnode, AVLTree)
        equilibrado = True
    if node.rightnode.bf > 0 and equilibrado == False:
      rotateRight(AVLTree, node.rightnode)
      rotateLeft(AVLTree, node)
      balancearriba(node, AVLTree)
    elif equilibrado == False:
      rotateLeft(AVLTree, node)
      balancearriba(node, AVLTree)
  else:
    if node.leftnode != None:
      reBalanceR(node.leftnode, AVLTree)
    if node.rightnode != None:
      reBalanceR(node.rightnode, AVLTree)

def balancearriba(node, AVLTree):
  if node.leftnode == None and node.rightnode == None:
    node.leftsize = 0
    node.rightsize = 0
    node.bf = 0
  elif node.leftnode != None and node.rightnode != None:
    if node.leftnode.rightsize > node.leftnode.leftsize:
      node.leftsize = node.leftnode.rightsize + 1
    else:
      node.leftsize = node.leftnode.leftsize + 1
    if node.rightnode.rightsize > node.rightnode.leftsize:
      node.rightsize = node.rightnode.rightsize
    else:
      node.rightsize = node.rightnode.leftsize
    node.bf = node.leftsize - node.rightsize
  elif node.leftnode != None:
    if node.leftnode.rightsize > node.leftnode.leftsize:
      node.leftsize = node.leftnode.rightsize + 1
    else:
      node.leftsize = node.leftnode.leftsize + 1
    node.rightsize = 0
    node.bf = node.leftsize
  else:
    node.leftsize = 0
    if node.rightnode.rightsize > node.rightnode.leftsize:
      node.rightsize = node.rightnode.rightsize
    else:
      node.rightsize = node.rightnode.leftsize
    node.bf = - node.rightsize
  if node.bf > 1 or node.bf < -1:
    reBalanceR(node, AVLTree)
  elif node.parent != None:
    balancearriba(node.parent, AVLTree)

def insert(AVLTree, element, key):
  if AVLTree.root == None:
    return
  else:
    newnode = AVLNode()
    newnode.value = element
    newnode.key = key
    insertR(newnode, AVLTree.root)
    balancearriba(newnode, AVLTree)

def insertR(newnode, cur):
  if newnode.key > cur.key:
    if cur.rightnode != None:
      return insertR(newnode, cur.rightnode)
    else:
      cur.rightnode = newnode
      newnode.parent = cur
      return newnode.key
  else:
    if cur.leftnode != None:
      return insertR(newnode, cur.leftnode)
    else:
      cur.leftnode = newnode
      newnode.parent = cur
      return newnode.key
  

def search(B,element):
  return searchR(B.root, element)
  
def searchR(cur, element):
  if cur.value == element:
    return cur.key
  if cur.leftnode != None:
    key = searchR(cur.leftnode, element)
    if key != None:
      return key
  if cur.rightnode != None:
    key = searchR(cur.rightnode, element)
    if key != None:
      return key
  return None

def delete(B,element):
  if B.root == None:
    return None
  if B.root.value == element:
    return root_deleted(B)
  else:
    nodetocheck = deleteR(B.root, element)
    if nodetocheck != None:
      balancearriba(nodetocheck, B)

def root_deleted(B):
  cur = B.root
  nodetocheck = None
  if cur.leftnode == None and cur.rightnode == None:
    B.root = None
  elif cur.leftnode == None and cur.rightnode != None:
    chosen = MenordesusMayores(cur)
    if cur.rightnode != chosen:
      nodetocheck = chosen.parent
      chosen.rightnode = cur.rightnode
      chosen.parent.leftnode = None
    else:
      nodetocheck = chosen
    chosen.parent = None
    B.root = chosen
  else:
    chosen = MayordesusMenores(cur)
    if cur.leftnode != chosen:
      nodetocheck = chosen.parent
      chosen.leftnode = cur.leftnode
      chosen.parent.rightnode = None
    else:
      nodetocheck = chosen
    chosen.rightnode = cur.rightnode
    chosen.parent = None
    B.root = chosen
  return nodetocheck

def deleteR(cur, element):
  if cur.value == element:
    if cur.leftnode == None and cur.rightnode == None:
      nodetocheck = cur.parent
      if cur.parent.leftnode == cur:
        cur.parent.leftnode = None
      else:
        cur.parent.rightnode = None
    elif cur.leftnode == None and cur.rightnode != None:
      chosen = MenordesusMayores(cur)
      if cur.rightnode != chosen:
        nodetocheck = chosen.parent
        chosen.rightnode = cur.rightnode
        chosen.parent.leftnode = None
      else:
        nodetocheck = chosen
      chosen.parent = cur.parent
      if cur.parent.leftnode == cur:
        cur.parent.leftnode = chosen
      else:
        cur.parent.rightnode = chosen
    else:
      chosen = MayordesusMenores(cur)
      if cur.leftnode != chosen:
        nodetocheck = chosen.parent
        chosen.leftnode = cur.leftnode
        chosen.parent.rightnode = None
      else:
        nodetocheck = chosen
      chosen.rightnode = cur.rightnode
      chosen.parent = cur.parent
      if cur.parent.leftnode == cur:
        cur.parent.leftnode = chosen
      else:
        cur.parent.rightnode = chosen
    return nodetocheck
  if cur.leftnode != None:
    nodetocheck = deleteR(cur.leftnode, element)
    if nodetocheck != None:
      return nodetocheck
  if cur.rightnode != None:
    nodetocheck = deleteR(cur.rightnode, element)
    if nodetocheck != None:
      return nodetocheck
  return None

def MayordesusMenores(cur):
  return Mayor(cur.leftnode)

def Mayor(cur):
  if cur.rightnode != None:
    return Mayor(cur.rightnode)
  else:
    return cur

def MenordesusMayores(cur):
  return Menor(cur.rightnode)

def Menor(cur):
  if cur.leftnode == None:
    return cur
  else:
    return Menor(cur.leftnode)

def deletekey(B, key):
  if B.root == None:
    return None
  if B.root.key == key:
    return root_deleted(B)
  else:
    return deletekeyR(B.root, key)

def deletekeyR(cur, key):
  if cur.key == key:
    if cur.leftnode == None and cur.rightnode == None:
      if cur.parent.leftnode == cur:
        cur.parent.leftnode = None
      else:
        cur.parent.rightnode = None
    elif cur.leftnode == None and cur.rightnode != None:
      chosen = MenordesusMayores(cur)
      if cur.rightnode != chosen:
        chosen.rightnode = cur.rightnode
        chosen.parent.leftnode = None
      chosen.parent = cur.parent
      if cur.parent.leftnode == cur:
        cur.parent.leftnode = chosen
      else:
        cur.parent.rightnode = chosen
    else:
      chosen = MayordesusMenores(cur)
      if cur.leftnode != chosen:
        chosen.leftnode = cur.leftnode
        chosen.parent.rightnode = None
      chosen.rightnode = cur.rightnode
      chosen.parent = cur.parent
      if cur.parent.leftnode == cur:
        cur.parent.leftnode = chosen
      else:
        cur.parent.rightnode = chosen
    return cur.key
  elif key > cur.key:
    if cur.rightnode != None:
      return deletekeyR(cur.rightnode, key)
    else:
      return None
  else:
    if cur.leftnode != None:
      return deletekeyR(cur.leftnode, key)
    else:
      return None

def access(B,key):
  return accessR(B.root, key)

def accessR(cur, key):
  if cur == None:
    return None
  elif cur.key == key:
    return cur.value
  elif key > cur.key:
    return accessR(cur.rightnode, key)
  else:
    return accessR(cur.leftnode, key)

def update(B, element, key):
  return updateR(B.root, element, key)

def updateR(cur, element, key):
  if cur == None:
    return None
  elif cur.key == key:
    cur.value = element
    return cur.key
  elif key > cur.key:
    return accessR(cur.rightnode, key)
  else:
    return accessR(cur.leftnode, key)

def traverseInPreOrder(B):
  L = LinkedList()
  traverseInPreOrderR(L, B.root)
  inversa(L)
  return L

def traverseInPreOrderR(L, cur):
  if cur == None:
    return None
  else:
    add(L, cur.value)
    traverseInPreOrderR(L, cur.leftnode)
    traverseInPreOrderR(L, cur.rightnode)

def traverseInOrder(B):
  L = LinkedList()
  traverseInOrderR(L, B.root)
  inversa(L)
  return L

def traverseInOrderR(L, cur):
  if cur == None:
    return None
  else:
    traverseInOrderR(L, cur.leftnode)
    add(L, cur.value)
    traverseInOrderR(L, cur.rightnode)

def traverseInPostOrder(B):
  L = LinkedList()
  traverseInPostOrderR(L, B.root)
  inversa(L)
  return L

def traverseInPostOrderR(L, cur):
  if cur == None:
    return None
  else:
    traverseInPostOrderR(L, cur.leftnode)
    traverseInPostOrderR(L, cur.rightnode)
    add(L, cur.value)

def traverseBreadFirst(B):
  queue = LinkedList()
  valuesQueue = LinkedList()
  enqueue(queue, B.root)
  while queue.head != None:
    node = dequeue(queue)
    enqueue(valuesQueue, node.value)
    if node.leftnode != None:
      enqueue(queue, node.leftnode)
    if node.rightnode != None:
      enqueue(queue, node.rightnode)
  inversa(valuesQueue)
  return valuesQueue