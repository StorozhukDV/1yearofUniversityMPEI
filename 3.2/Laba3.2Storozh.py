import sys
import math

i=0 #индекс массива
n=0 #количество элементов массива
Nmax=n   # максимальный размер массива
s=" " # рабочая строка для считывания строк из файла
s_in =[] #строка для преобразования в числа
ch=","
Max=0.0
proizv=0   # модуль произведения

input('Нажмите Enter для запуска программы')
print('Лабораторня работа 3.2')
print('Ввод массива из файла')

nameF = sys.argv[1]

fd=open(nameF,'r') # открытие исходного текстового файла файла в режиме чтения
n=int(fd.readline()) # преобразование прочитанной строки в целочисленный тип данных
Mas_dub1=[0.0]*n #Объявление массива
Mas_dub2=[0.0]*n
print('Число элементов в массиве = ', n)
print()

s=fd.readline()
print('Введен массив', s)
print()

s_in=s.split(ch)
print(s_in)
print()

for i in range(n):
    Mas_dub1[i]=float(s_in[i])
print('Вывод массива', Mas_dub1)
print()

s=fd.readline()
print('Введен массив', s)
print()

s_in=s.split(ch)
print(s_in)
print()

for i in range(n):
    Mas_dub2[i]=float(s_in[i])
print('Вывод массива', Mas_dub2)
print()
fd.close()

Max=abs(Mas_dub1[0]*Mas_dub2[n-1])
for i in range (1,n):  # цикл проверки со второго элемента массива А и второго с конца массива С
        proizv=abs(Mas_dub1[i]*Mas_dub2[n-i-1])
        if proizv>Max:
                Max=proizv
print('Наибольшая из абсолютных величин произведений равна {:.2f}'.format(Max))

    
