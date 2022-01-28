#Проверка условия
def Prov (A,n,i,j):
    flag1=False
    Max = 0 # максимальный положительный четный элемент
    for i in range (0,n-1,1):
        if A[i][j]%2==0:
            print(1000000000001)
            if flag1==False:
                Max=A[i][j]
                flag1=True
                print(1000000000002)
        else:
            if A[i][j]>Max and A[i][j]%2==0:
                Max=A[i][j]
    return flag1,Max
                
            
            
        
        
