from matrica import*
from zadachi import*
print('___Типовик___','\n')

flag1 = True # флаг выполнения условия
flag2 = True # флаг алльтернативы
flag3 = True # флаг алльтернативы
num = 0 # номер первого эл >c в столбце
Max = 0 # максимальный положительный эл в столбце
    
A,n,m,c=vvod()

print ('Исходная матрица:','\n')
vivod(A,n,m)
print ('Значение C = ',c,'\n')

for j in range (0,m,2): # цикл по четным столбцам
        flag1 = Prov (A,n,c,j)

        #Если условие выполнено 
        if flag1==True:
            print('Условие для ',j+1,'-го столбца выполнено, ищем элементы в столбце ',j+2,', значение которых больше ',c)
            flag2, num = Num (A,n,c,j)
            if flag2==True:
                print ('В след.столбце ',j+2,' нет элементов, значение которых больше ',c,'\n')
            else:
                print('В столбце ',j+2,',индекс элемента, значение которого больше C = ',c,', равен: ',num+1,'\n')

         #Если условие НЕ выполнено 
        else:
            print('Сумма элементов ',j+1,'-го столбца ,больше С следовательно, ищем максимальный, среди положительных элементов в столбце')
            flag3,Max = MaxPos (A,n,j)
            if flag3==True:
                print ('В столбце ',j+1,' нет положительных элементов','\n')
            else:
                print ('Максимальный, среди положительных элементов в столбце ',j+1,' равен ',Max,'\n')

        
input()
