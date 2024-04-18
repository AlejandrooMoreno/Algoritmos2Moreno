from trie import*

def mismoDocumento(T1, T2):
  if T1.root == None and T2.root == None:
    return True
  elif (T1.root == None and T2.root != None) or (T1.root != None and T2.root == None):
    return False
  else:
    return comparar(T1.root, T2.root)

def comparar(node1, node2):
  if node1.children == None and node2.children == None:
    return True
  elif (node1.children == None and node2.children != None) or (node1.children != None and node2.children == None):
    return False
  elif len(node1.children) != len(node2.children):
    return False
  else:
    tamaño = len(node1.children)
    for x in range(0, tamaño):
      sonIguales = False
      for i in range(0, tamaño):
        if node1.children[x].key == node2.children[i].key:
          if node1.children[x].isEndOfWord == node2.children[i].isEndOfWord:
            sonIguales = comparar(node1.children[x], node2.children[i])
            break
          else:
            return False
      if sonIguales == False:
        return False
    return True