from zadacha import*

Nmax=10 #размерность матрицы
n=0 #po vertikali
m=0 #po gorizonty
i=j=0
c=0 #kolvo elementov massiva
R=0 #znachenie s ruki
A=[0.0]*Nmax
flag1 = True
p=1

for i in range (Nmax):
    A[i]=[0]*Nmax
n=int(input('VVedite kolichestvo strok'))
print('n= ',n)

m=int(input('VVedite kolichestvo stolbcov'))
print('m= ',m)


for i in range(n):
    for j in range (m):
        print('Vvvedite element',p)
        p+=1
        A[i][j]=float(input())


print ('Vvedenniya matriza:','\n')
for i in range (n):
        for j in range (m):
                print('{:^6.1f}'.format(A[i][j]), end=' ')
        print()

R=int(input('VVedite znachenie R '))
print ("Znechenie R=",R,'\n')



flag1,Max = Prov (A,n,i,j)
print(1000000000003)

#esli est chetnie elemnt
if flag1==True:
    print("est chetnie")
    if Max>R:
        print('Uslovie vipoln')
    else:
        print('Uslovie ne vipol')
else:
    print("net chetnich")

input()

            
            
