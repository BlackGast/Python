import random as random
from random import randint

#def coast():
#    a=int(input("Введите цену 1 кг конфет: "))
#    b=int(input("Введите цену 1 кг печенья: "))
#    c=int(input("Ведите сколько покупок хотите совершить: "))
#    if int(c)==1:
#        print("стоимость конфет за 300 гр: ", a*0.3)
#        print("Стоимость печенья за 400 гр: ", b*0.4)
#    if int(c)==3:
#        print("Стоимость конфет за 1.8 кг: ", c*a*1.8)
#        print("Стоимость печения за 2 кг: ", c*b*2)
#    else:
#        print("Введие 1 или 3 покупки")
##coast()

#def Array():
#    array=[]
#    array.append(54)
#    temp = array[0]
#    i = 0
#    while (temp < 9154):
#        i += 1
#        array.append(array[i-1] + 5)
#        temp = array[i]


##i=0
##for i in range(0,31):
##    if i%2:
##        if i==8 or i == 19:
##            break
##        if i==3 or i==10:
##            continue
##        else:
##            print(i)

##def string(a):
##    print(len(a))

##    print(a.index("сопровождать"))

##    print(a.count("о"))

##    print(a.split(","))

##    b=a.split(",")
##    c=a[3]
##    b=c.split(" ")
##    print(ord(b[0]))
##    d="где"
##    print(ord(d))
##string("Пишите код так, как будто сопровождать его будет склонный к насилию психоват, который знает, где вы живете")

#class drob:
#    def __init__(self, a, b):
#        self.a=a
#        self.b=b
#    def __eq__(self, other):
#        if self.a == other.a or self.b == other.b:
#            return True
#        return False



#def pr1(a,b): #Задание 1 Готово
#    print((a+4*b)*(a-3*b)+a**2)
#pr1(2,3)

#def pr2(): #Задание 2
#    array=[]
#    i=0
#    while i<10:
#        array.append(random.randint(1,20))
#        i += 1
#    print(array)
#    avg=0
#    for i in range(len(array)):
#        avg+=array[i]
#    avg/=len(array)
#    for i in range(len(array)):
#        if array[i]>10:
#            array[i]=avg
#    print(array)
#pr2()

#def pr3(a): #Задание 3 Готово
#    t=0
#    y=3
#    b=0
#    while t!=3:
#        t+=1
#        if a[t] < a[t-1]:
#            b+=1
#    if b<3:
#        print("Нет")
#    else:
#        print("Да")
        
#a=[4,3,2,1]
#pr3(a)

def student():
    n=int(input("Количестко учащихся"))
    p=4
    array=[]
    for i in n:
        podarray=[]
        for j in p:
            podarray.append(randint(1,5))
    for i in array:
        for j in i:
            print(j, end=" ")
        print()
student()