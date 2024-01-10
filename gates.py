def _and(a, b):
    if a == b:
        if a == True:
            return True
    else:
        return False

def _or(a, b):
    if a == True:
        return True
    elif b == True:
        return True
    else: return False

def _not(a, b):
    if a != b:
        return True
    else:
        return False

def _nand(a, b):
    if a == b:
        if a == True:
            return False
    else: return True

def _xor(a, b):
    if a == True:
        if b ==False:
            return True
        else: return False
    if b == True:
        if a ==False:
            return True
def _xnor(a, b):
    if a == b:
        return True
    else: return False
