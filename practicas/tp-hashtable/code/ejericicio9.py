class dictionary:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def __str__(self):
        return str(self.array)

class dicNode:
  value = None
  key = None

def H(k, tamaño):
  A = (5^(1/2) - 1) / 2
  return math.floor(tamaño * (k * A - math.floor(k * A)))

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