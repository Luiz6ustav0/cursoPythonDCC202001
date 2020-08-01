def head(L):
    if not L:
        return None
    return L[0]
 
def tail(L):
    if not L:
        return None
    return L[1]

def py2ll(L):
    if not L:
        return None
    return (L[0], py2ll(L[1:]) )

def ll2py(L):
    if not L:
        return []
    H = head(L)
    T = tail(L)
    return [H] + ll2py(T) 

def size(L):
    if not L:
        return 0
    return 1 + size(tail(L))

def sorted(L):
    if not L:
        return True
    elif not tail(L):
        return True
    else:
        C1 = head(L) <= head(tail(L))
        return C1 and sorted(tail(L))

def sum(L):
    if not L:
        return 0
    if not tail(L):
        return head(L)
    else:
        H0 = head(L)
        return H0 + sum(tail(L))

def split(L):
    if not L:
        return (None, None)
    if not tail(L):
        return (L, None)
    head_0 = head(L)
    head_1 = head(tail(L))
    (tail_0, tail_1) = split(tail(tail(L)))
    return ( (head_0, tail_0), (head_1, tail_1) )

def merge(L0, L1):
    if not L0:
        return L1
    if not L1:
        return L0
    else:
        H0 = head(L0)
        H1 = head(L1)
        T0 = tail(L0)
        T1 = tail(L1)
        if H0 < H1:
            return (H0, merge(T0, L1))
        return (H1, merge(L0, T1))

def mSort(L):
    if not L:
        return None     
    elif not tail(L):
        return L
    else:
        (L0, L1) = split(L)
        return merge(mSort(L0), mSort(L1))

def max(L):
    if not L:
        return None
    if not tail(L):
        return head(L)
    else:
        num = head(L)
        nxt = max(tail(L))
        if(num > nxt):
            return num
        return nxt

def get(L, N):
    if N == 0:
        return head(L)
    if N > 0:
        return get(tail(L), N-1)