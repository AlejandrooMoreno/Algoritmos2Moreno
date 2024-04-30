def comprimir_cadena(palabra):
  palabra_comprimida = palabra[0]
  ultima_letra = palabra[0]
  repetido = 1
  for x in range(1, len(palabra)):
    if palabra[x] == ultima_letra:
      repetido += 1
    else:
      palabra_comprimida = palabra_comprimida + str(repetido) + palabra[x]
      if len(palabra_comprimida) >= len(palabra):
        return palabra
      ultima_letra = palabra[x]
      repetido = 1
  palabra_comprimida = palabra_comprimida + str(repetido)
  if len(palabra_comprimida) < len(palabra):
    return palabra_comprimida
  else:
    return palabra