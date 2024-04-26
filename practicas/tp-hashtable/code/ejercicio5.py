from dictionary import*

def elementosunicos(L):
    if len(L) == 1:
        return True
    else:
        D = dictionary()
        insert(D, L[0], L[0])
        for x in range(1, len(L)):
            if search(D, L[x]) == L[x]:
                return False
            else:
                insert(D, L[x], L[x])
        return True