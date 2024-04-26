class dictionary:
    def __init__(self, length=9):
        self.dictionary = [[] for _ in range(length)]

    def __getitem__(self, key):
        return self.dictionary[key]

    def __str__(self):
        return str([item for item in self.dictionary])

class dicNode:
  value = None
  key = None

def H(k):
  return k % 9

def insert(D, key, value):
  newnode = dicNode()
  newnode.value = value
  newnode.key = key
  D[H(key)].append(newnode)
  return D

def search(D,key):
  position = H(key)
  for x in range(0, len(D[position])):
    if D[position][x].key == key:
      return D[position][x].value
  return None

def delete(D,key):
  position = H(key)
  for x in range(0, len(D[position])):
    if D[position][x].key == key:
      D[position].pop(x)
      return D
  return D