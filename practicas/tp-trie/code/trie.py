class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def insert(T, element):
    if T.root == None:
        T.root = TrieNode()
    insertR(0, T.root, element)
    return T

def insertR(i, node, element):
    if node.children == None:
        newnode = TrieNode()
        newnode.key = element[i]
        node.children = [newnode]
        newnode.parent = node
        if i + 1 < len(element):
            return insertR(i + 1, newnode, element)
        else:
            newnode.isEndOfWord = True
            return
    else:
        for x in range(0, len(node.children)):
            if node.children[x].key == element[i]:
                if i + 1 < len(element):
                    return insertR(i + 1, node.children[x], element)
                else:
                    node.children[x].isEndOfWord = True
                    return
        newnode = TrieNode()
        newnode.key = element[i]
        node.children.append(newnode)
        newnode.parent = node
        if i + 1 < len(element):
            return insertR(i + 1, newnode, element)
        else:
            newnode.isEndOfWord = True

def search(T,element):
    if T.root == None:
        return False
    else:
        return searchR(0, T.root, element)

def searchR(i, node, element):
    if node.children == None:
        return False
    else:
        for x in range(0, len(node.children)):
            if node.children[x].key == element[i]:
                if i + 1 < len(element):
                    return searchR(i + 1, node.children[x], element)
                elif node.children[x].isEndOfWord == True:
                    return True
                else:
                    return False
        return False

def delete(T, element):
    if T.root == None:
        return False
    else:
        eliminado, tieneHijos = deleteR(0, T.root, element)
        return eliminado

def deleteR(i, node, element):
    if node.children == None:
        return False, None
    else:
        for x in range(0, len(node.children)):
            if node.children[x].key == element[i]:
                if i + 1 < len(element):
                    eliminado, tieneHijos = deleteR(i + 1, node.children[x], element)
                    if eliminado == True:
                        if tieneHijos == False:
                            if node.children[x].isEndOfWord == True:
                                return True, True
                            else:
                                node.children.pop(x)
                                return True, False
                        else:
                            return eliminado, tieneHijos
                    else:
                        return eliminado, tieneHijos
                elif node.children[x].isEndOfWord == True:
                    if node.children[x].children != None:
                        node.children[x].isEndOfWord = False
                        return True, True
                    else:
                        node.children.pop(x)
                        return True, False    
                else:
                    return False, None
        return False, None

def autoCompletar(T, cadena):
    if T.root == None:
        return ""
    else:
        return encontrarcadena(0, T.root, cadena)

def encontrarcadena(i, node, cadena):
    if node.children == None:
        return ""
    else:
        for x in range(0, len(node.children)):
            if node.children[x].key == cadena[i]:
                if i + 1 == len(cadena):
                    return restante(node.children[x], "")
                else:
                    return encontrarcadena(i + 1, node.children[x], cadena)
        return ""

def restante(node, element):
    if node.children == None:
        return element
    elif len(node.children) > 1:
        return element
    elif node.children[0].isEndOfWord == False:
        return restante(node.children[0], element + node.children[0].key)
    else:
        return element + node.children[0].key