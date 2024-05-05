import math

def h(codigo_postal):
  key = ord(codigo_postal(0))
  for x in range(1, 5):
    key = int(codigo_postal(x))
  for x in range(5, 8):
    key = ord(codigo_postal(x))
  A = (5^(1/2) - 1) / 2
  return math.floor(1328602500 * (key * A - math.floor(key * A)))