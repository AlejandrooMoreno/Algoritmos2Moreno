def ContieneSuma(A,n):
    izquierda = 0
    derecha = len(A) - 1
    A.sort()
    while izquierda != derecha:
        if A[izquierda] + A[derecha] == n:
            return True
        elif A[izquierda] + A[derecha] < n:
            izquierda += 1
        else:
            derecha -= 1
    return False