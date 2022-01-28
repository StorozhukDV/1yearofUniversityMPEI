#Проверка условия
def Prov (A,n,c,j):
    summ=0
    for i in range(n):
            flag1 = False
            summ+=A[i][j]

    if summ<c:
            flag1=True
    return flag1
#Если условие выполнено
def Num (A,n,c,j):
    j+=1
    i=0 # индексация строк
    num=0 # индекс первого эл >с1
    flag2 = True # флаг поиска первого эл >с1
    while i<n and flag2==True:
            if A[i][j]>c:
                    num=i
                    flag2=False
            else:
                    i+=1
    return flag2, num

def MaxPos (A,n,j):
    Max=0 # максимальный, среди положительных
    flag3 = True # флаг альтернативы
    for i in range (n):
        if A[i][j]>0:
            if flag3==True:
                Max=A[i][j]
                flag3 = False
            else:
                if A[i][j]>Max:
                    Max=A[i][j]
    return flag3, Max
    
