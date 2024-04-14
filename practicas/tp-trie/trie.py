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
        return None
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
