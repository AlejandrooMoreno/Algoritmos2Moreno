class dictionary:
    def __init__(self):
        self.size = 9
        self.elements = [None] * self.size

    def __getitem__(self, key):
        return self.elements[key]

    def __setitem__(self, key, value):
        self.elements[key] = value

    def __str__(self):
        return str(self.elements)

class dicNode:
  value = None
  key = None

def H(k):
  return k % 9

def insert(D, key, value):
  newnode = dicNode()
  newnode.value = value
  newnode.key = key
  position = H(key)
  if D[position] == None:
    newlist = [newnode]
    D[position] = newlist
  else:
    D[position].append(newnode)
  return D

def search(D,key):
  position = H(key)
  if D[position] != None:
    for x in range(0, len(D[position])):
      if D[position][x].key == key:
        return D[position][x].value
  return None

def delete(D,key):
  position = H(key)
  if D[position] != None:
    for x in range(0, len(D[position])):
      if D[position][x].key == key:
        if len(D[position]) == 1:
          D[position] = None
        else:
          D[position].pop(x)
        return D
  return D