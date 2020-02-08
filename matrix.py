def matrix(n=None, m=1, a=0):
    if not n:
        n = m
    elif n and m == 1:
        m = n

    return [[a for j in range(m)] for i in range(n)]
