def mitadmenores(L):
    if len(L) > 2:
        L.sort()
        tamaño = len(L)
        if tamaño % 2 == 0:
            element = L[tamaño - 2]
            L.pop(tamaño - 2)
        else:
            element = L[tamaño - 1]
            L.pop()
        L.insert(round(tamaño/2) - 1, element)
        return L