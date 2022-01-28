import sys
import parallelepiped as p
print ('Лабораторная работа № 7','\n')

### Раздел констант
nMax = 10

### Раздел переменных
fd = '' # рабочая строка для чтения из файла
flg = True # флаг условия
k = 0 #количество случаев
V=0 #  объем оставшегося материала
minV = 0 # минимальные остатки материала
maxV = 0 # максимальные остатки материала
i = 0 # индекс набора значений
n = 0 # количество наборов значений
pList = [p.Parallelepiped() for i in range (nMax)] # создаем массив (список) из отдельных объектов

#считываем данные из файла и вывод на экран
nameF = 'dat1.txt'
if len(sys.argv)>1:
    nameF = sys.argv[1]
infile=open(nameF,'r')
n=int(infile.readline())
if n>nMax:
    n = Nmax
print ('{0:^8}|{1:^8}|{2:^8}|{3:^8}|{4:^8}'.format('№ набора','R','A','B','С'),'\n')
for i in range(n):
    fd = infile.readline() 
    R,A,B,C = fd.split()
    pList[i] = p.Parallelepiped (R,A,B,C) 
    print ('{0:^8d}|{1:^8.1f}|{2:^8.1f}|{3:^8.1f}|{4:^8.1f}'.format(i+1,pList[i].r,pList[i].a,pList[i].b,pList[i].c),'\n')
infile.close() # закрываем файл


for i in range(n):
    flg = pList[i].check()
    if flg: # соответствует условию
        k+=1
        V=pList[i].ostatok()

        if k==1:
            minV = V
            maxV = V            
        else:
            if V<minV:
                minV = V
            if V>maxV:
                maxV = V

if k==0:
    print('Невозможно выпилить параллелепипеды из шаров с данными значениями')

elif minV==maxV:
    print ('Количество получившихся брусьев: ',k,' из ',n,'\n')
    print ('Обем остатков материала для случаев, когда параллелепипед может быть выпилен из шара равен: {:.2f}'.format(minV))
else:
    print ('Количество получившихся брусьев: ',k,' из ',n,'\n')
    print ('Минимальный объем остатка: {:.2f}'.format(minV),'\n')
    print ('Максимальный объем остатка: {:.2f}'.format(maxV))
