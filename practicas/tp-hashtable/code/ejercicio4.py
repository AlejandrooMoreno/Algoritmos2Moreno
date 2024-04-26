def permutacion(s, p):
    if len(s) != len(p):
        return False
    else:
        list1 = list(s)
        list2 = list(p)
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else: 
            return False