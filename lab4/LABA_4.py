import math as t 
MAX_COUNT=2500 
x=(-0.98, -0.5, 0.1, 0.5, 0.95)
i=0 
j=0 

sums=0.0 
Func=0.0 
s_i=0.0 
eps=0.0
S_F=0.0 

k=0 
z=0 
zs=''
format_s=''
print('                       Лабораторная работа 4')
eps=float(input('введите eps в диапазоне : 0<eps<=0.1:\n '))
print(eps)

for j in range (len(x)):
    print(x[j])
z= t.ceil( abs(t.log(eps)/t.log(10)) )+1
zs=str(z)
print('eps={0:e}'.format(eps)) 

print('N |        X        |       S(X)      | K  |       F(X)      |   |S(X)-F(X)|   |')
for k in range(0,80,1):
    print('=', end='')   
for j in range (len(x)):
    i=1 
    s_i=(x[j]**2)
    sums=s_i
    while not(t.fabs(s_i)<eps) and (i !=MAX_COUNT): 
        i+=1 
        s_i=(-s_i)*((i-1)*(2*i-3)*x[j]**2/(i*(2*i-1)))
        sums=sums+s_i 
    Func=2*x[j]*t.atan(x[j])-2*t.log(t.sqrt(1+x[j]**2))
    S_F=t.fabs(sums-Func)
    format_s='{0:2d}|{1:17.' +zs+ 'f}|{2:17.' +zs+ 'f}|{3:4d}|{4:17.' +zs+ 'f}|{5:17.' +zs+ 'f}|' 
    print(format_s.format(j+1, x[j], sums,i,Func, S_F))
