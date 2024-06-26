from trie import*

def prefijocomun(T, p, n):
  if T.root == None:
    return
  else:
    return prefijoR(0, p, n, "", T.root)

def prefijoR(i, p, n, element, node):
  if node.children == None:
    return
  elif i < len(p):
    for x in range(0, len(node.children)):
      if node.children[x].key == p[i]:
        element = element + p[i]
        if i + 1 < n:
          return prefijoR(i + 1, p, n, element, node.children[x])
        elif node.children[x].isEndOfWord == True and i + 1 == len(p):
          print(element)
          return
        else:
          return
    return
  elif i < n:
    for x in range(0, len(node.children)):
      if i + 1 == n:
        if node.children[x].isEndOfWord == True:
          print(element + node.children[x].key)
        else:
          return
      else:
        prefijoR(i + 1, p, n, element + node.children[x].key, node.children[x])