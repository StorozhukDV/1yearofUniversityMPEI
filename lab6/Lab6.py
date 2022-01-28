print('___Laba6___','\n')
import sys

Nmax=10 #максимальная размерность матрицы
n=0 #реальная размерность матрицы по вертикали
m=0 #реальная размерность матрицы по горизонтали
i=j=0 # индексы
c=0 # задаваемое пользователем значение
s_in= [0.0]*Nmax #пустой массив для значений строки, после ее разделения
inputstr='' #рабочая строка для чтения матрицы из файла
A=[0.0]*Nmax #пустой массив максимального размеpa

summ=0 # сумма элементов столбца

   
num = 0 # номер первого элемента >c в столбце
Max = 0 # максимальный положительный элемента в столбце

nameF=sys.argv[1] #имя файла
fd=open(nameF,'r') #открываем файл для чтения

n=int(fd.readline()) #реальная размерность матрицы по вертикали
if n>Nmax:
        Nmax=n
m=int(fd.readline()) #реальная размерность матрицы по горизонтали
if m>Nmax:
        Nmax=m

c=int(fd.readline())
        
        
for j in range(Nmax):
        A[j]=[0]*Nmax 

#считывание
for i in range(n):
        inputstr=fd.readline() #чтение строки
        s_in=inputstr.split() #разделение строки
        for j in range(m):
                A[i][j]=float(s_in[j])

fd.close()

print ('Vvedenniya matriza:','\n')
for i in range (n):
        for j in range (m):
                print('{:^6.1f}'.format(A[i][j]), end=' ')
        print()
                
print ('Значение C = ',c,'\n')

#Проверка условия
for j in range (0,m,2): # цикл по четным столбцам
        summ=0
        num=0
        Max=0
        for i in range(n):
                flag1 = False
                summ+=A[i][j]

        if summ<c:
                flag1=True
#Если условие выполнено
        if flag1==True:
                print('Условие для ',j+1,'-го столбца выполнено, ищем элементы в столбце ',j+2,', значение которых больше ',c)
                j+=1
                i=0
                flag2 = True
                while i<n and flag2==True:
                        if A[i][j]>c:
                                num=i
                                flag2=False
                        else:
                                i+=1
                if flag2==True:
                        print ('В след.столбце ',j+1,' нет элементов, значение которых больше ',c,'\n')
                else:
                        print('В столбце ',j+1,',индекс элемента, значение которого больше C = ',c,', равен: ',num+1,'\n')
#Если условие не выполнено
        else:
                flag3 = True
                print('Сумма элементов ',j+1,'-го столбца ,больше С следовательно, ищем максимальный, среди положительных элементов в столбце')
                for i in range (n):
                        if A[i][j]>0:
                            if flag3==True:
                                Max=A[i][j]
                                flag3 = False
                            else:
                                if A[i][j]>Max:
                                    Max=A[i][j]
                if flag3==True:
                        print ('В столбце ',j+1,' нет положительных элементов','\n')
                else:
                        print ('Максимальный, среди положительных элементов в столбце ',j+1,' равен ',Max,'\n')
input()

