import math
import time 

x=y=0.0 #koordinati tochek
S=6 #ploshad max romba
n=0 #число точек
i=0 #s4et4ik cikla
kol=0 #kol-vo tochek, popavshih v promezhutok
flag=False #flazhok popadani9
S1=0.0 #Ploshad robma is koord
D1=0.0 #Ploshad treugolnikov ia koord
S3=0.0 #Ploshad figuti is koordinat

print('Laba number two')

n=int(input('Vvod n>>')) 
print('chislo to4ek>>',n)

for i in range(n):
    print(i)
    x=float(input('Vvod x>>'))
    y=float(input('vvod y>>'))
    print('X,Y>>',x,y)
    S1=((math.fabs(x)*2)*(math.fabs(y)*2))/2
    D1=(math.fabs(x)*(math.fabs(y)*2))*0.125
    S3=S1-D1
    flag=(S3)<=S and (x<=1) and (x>=-1) and (y<=2) and (y>=-2)
    if flag: #if flag==True:
        kol+=1 #kol=kol+1
if kol!=0:
    print('kol-vo popavshih to4ek>>',kol)
else:
    print('net popavshih to4ek')
time.sleep(650)


    
