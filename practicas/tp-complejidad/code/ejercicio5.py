def ContieneSuma(A,n):
    izquierda = 0
    derecha = izquierda + 1
    while izquierda < len(A):
        if A[izquierda] >= n:
            izquierda += 1
            derecha = izquierda + 1
        else:
            while derecha < len(A):
                if A[izquierda] + A[derecha] == n:
                    return True
                else:
                    derecha += 1
            izquierda += 1
            derecha = izquierda + 1
    return False