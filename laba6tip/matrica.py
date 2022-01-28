def vvod ():
    import sys

    Nmax=10 #максимальная размерность матрицы
    n=0 #реальная размерность матрицы по вертикали
    m=0 #реальная размерность матрицы по горизонтали
    i=j=0 # индексы
    c=0 # задаваемое пользователем значение
    s_in= [0.0]*Nmax #пустой массив для значений строки, после ее разделения
    inputstr='' #рабочая строка для чтения матрицы из файла
    A=[0.0]*Nmax #пустой массив максимального размеpa
    
    nameF=sys.argv[1] #имя файла
    fd=open(nameF,'r') #открываем файл для чтения

    n=int(fd.readline()) #реальная размерность матрицы по вертикали
    if n>Nmax:
        Nmax=n
    m=int(fd.readline()) #реальная размерность матрицы по горизонтали
    if m>Nmax:
        Nmax=m
    print('Количество строк в матрице: ',n,'\n')
    print('Количество столбцов в матрице: ',m,'\n')

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

    return A,n,m,c

def vivod (A,n,m):
    i=0 # индекс строк
    j=0 # индекс столбцов

    for i in range (n):
        for j in range (m): 
            print('{:^6.1f}'.format(A[i][j]), end=' ')
        print()
    
