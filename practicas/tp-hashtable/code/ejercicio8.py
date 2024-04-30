def ocurrencia_enString(p, a):
  for x in range(0, len(a) - len(p) + 1):
    if a[x] == p[0]:
      primer_ocurrencia = x
      i = 1
      x += 1
      while x < len(a) and i < len(p):
        if a[x] == p[i]:
          if i == len(p) - 1:
            return primer_ocurrencia
          else:
            x += 1
            i += 1
        else:
          break