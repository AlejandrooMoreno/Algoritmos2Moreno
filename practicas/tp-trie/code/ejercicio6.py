from trie import*

def cadenasinvertidas(T):
  if T.root == None:
    return False
  else:
    return cadenasinvertidasR(T, T.root, "")
  
def cadenasinvertidasR(T, node, palabra):
  if node.children == None:
    return False
  else:
    for x in range(0, len(node.children)):
      if node.children[x].isEndOfWord == True:
        nueva_palabra = palabra + node.children[x].key
        invertida = nueva_palabra [:: - 1 ]
        if search(T, invertida) == True:
          return True
      if cadenasinvertidasR(T, node.children[x], palabra + node.children[x].key) == True:
        return True
    return False