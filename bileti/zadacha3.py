def u (A,h,n,i):
    import math as z
    j=0
    for i in range(n):
        h+=z.pow((z.sin(A[i][j])),3)
    return h
