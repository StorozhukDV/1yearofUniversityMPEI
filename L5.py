print('Лабораторная работа № 5','\n')

from sys import argv

i=0    
j=0    
n = 0  # размерность матрицы
Nmax = 10
Summ = 0  # Общая сумма элементов, удовлетворяющих условию
diagSumm = 0 # Сумма элементов главной диагонали
stSumm = 0 # сумма элементов столбца
A=[0.0]*Nmax 
for i in range(Nmax):
        A[i]=[0.0]*Nmax 
X=[0.0]*Nmax      

filename = argv[1]      
inputfile=open(filename,'r')    # открытие файла в режиме чтения
n=int(inputfile.readline())     # преобразование прочитанной строки в целочисленный тип файла

if n>10:
        n = Nmax

### Ввод исходной матрицы
for i in range(n):
        inputstr=inputfile.readline()   # чтение строки из файла
        X=inputstr.split(',')
        for j in range(n):
                A[i][j]=float(X[j])     # преобразование строки в вещественные числа
inputfile.close                         # закрытие файла

### Вывод исходной матрицы
print ('Исходная матрица:','\n')
for i in range (n):
   for j in range (n):
       print ('{:^5.1f}'.format(A[i][j])
               
### Проверка условия
for i in range (n):
   for j in range (n):
       diagSumm=0
for i in range(n):
                stSumm+=A[i][j]
              diagSumm+=A[j][j]
        if stSumm>0:
                Summ+=stSumm

print('Общая сумма элементов столбцов матрицы, суммы элементов в каждом из которых положительна: ',Summ,'\n')
print('Сумма элементов главной диагонали равна: ',diagSumm)
