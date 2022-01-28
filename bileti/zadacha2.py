def u (A,i,z):
    import math
    j=0
    s=0.0
    while j<z:
        s=(2*math.pi*A[i][j+1]*A[i][j])+(2*math.pi*((A[i][j+1])**2))
        j+=z
    return s
        
