import math as z
from zadacha3 import*

h=0
n=0
i=j=0
Nmax=10
A=[0.0]*Nmax

p=1

for i in range (Nmax):
    A[i]=[0]*Nmax
n=int(input('VVedite razmernost matrici '))

C=[0.0]*n
for i in range(n):
    for j in range(n):
        print('Vvvedite element',p)
        p+=1
        A[i][j]=float(input())
print('Vvedenya matrica','\n')
for i in range(n):
    for j in range(n):
        print('{:^6.1f}'.format(A[i][j]),end=' ')
    print()

for i in range(n):
    flag1=True
    while j<n and flag1==True:
        if A[i][j]==0:
            flag1=False
        else:
            j+=1
    if flag1==False:
        h=u(A,h,n,i)
        C[i]=h
    else:
        C[i]=z.fabs(A[i][i])
        
print('Poluchen massiv C','\n')
print(C)

input()
    
    
