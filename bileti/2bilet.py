import math
from zadacha2 import*

Nmax=10
A=[0]*Nmax
C=[0]*Nmax
s=0.0
n=int(input('Vvedite kol-vo celindrov: '))
z=2
i=j=0
k=0

for i in range(n):
    A[i]=[0.0]*z
    C[i]=float(input('Vvedite elementi massiva C '))

for i in range (n):
    for j in range (z):
        A[i][j]=float(input('Vvedite parametri cilindra: '))
print()

print('{0:^3}|{1:^3}|'.format('L','R'))
for i in range(n):
    for j in range(z):
        print(A[i][j],end=' ')

for i in range(n):
    s=u(A,i,z)
    if s>math.fabs(C[i]):
        k+=1
if k!=0:
    print('Kol-vo cilikov: ',k)
else:
    print('Net cilikov proshedshih proverku uslovia')


input()

        
