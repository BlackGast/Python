#a=5
#while a>0:
    #print(a)
    #a-=1
#print("Цикл закончен")

#a=int(input("Введите число\n"))
#b=0
#while a!=0:
#    b=b+a
#    a=int(input("Введите число\n"))
#print(b)

#for i in range(0,21,2):
#    print(i)

#a=int(input("Введите число"))
#for i in range(1,a+1):
#    print("*"*a)

#i=0
#while i<5:
#    a=int(input())
#    b=int(input())
#    if a==0 and b==0:
#        print("Пара нулей")
#        break
#    if a==0 or b==0:
#        continue
#    else:
#        print(a*b)
#    i+=1

#i=0
#while i<5:
#    a=int(input())
#    if a<10:
#        continue
#    elif a>100:
#        break
#    else:
#        print("Value access\n",a)
#    i+=1

def max(a,b):
    if a>b:
        return a
    else:
        return b

def ErroR():
    print("Ошибка")

#a=int(input())
#p=lambda a: a**1/2
#print(p(a))

def urav(x):
    if x<=-2:
        print(1-(x+2)**2)
    elif x>-2 and x<=2:
        print(-x/2)
    elif x>2:
        print(1+(x-2)**2)
    else:
        pass

print(urav(-3))