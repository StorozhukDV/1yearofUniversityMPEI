import time 
import math #biblioteka
x=0.0 #Arg. funkcii
y=0.0 #Rezultat
print('Лабораторная №1')
print()
x=float(input('Ввод X =: ')) #Ввод веществ. числа
print(x)
y=1/3*math.pow(math.exp(6.3+math.pow(x,1/2)),1/7)*abs(math.cos(2*x/3)-x)
print('Результат: ',y)
time.sleep(120)


       
