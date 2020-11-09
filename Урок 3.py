""" def func(s1,s2):
    s=s1+s2
    return s


x=input()
y=input()
print(func(x,y)) """

""" def strok(s1,s2):
    if s1>s2:
        return s1
    else:
        return s2

x=input()
y=input()
print(strok(x,y)) """

""" s=input()
a=s[1]
print(a) """

""" s=("A1-B2-C3-D4-E5")
a=s[3:10:3]
print(a) """

""" s=("Сегодня мы изучаем строки")
a=s[19:25]
print(a) """

""" def name(n):
    n=n.split(", ")
    for i in range(len(n)):
        x="Привет "+n[i]
        print(x)
        i+=1

name("Jak, Jane, Victor") """

""" a=[2,3,4,1]
b=a
a.append("a")
print(a)
print(b) """

""" a=[0]*5
print(a) """

""" a=[0 for i in range(5)]
print(a) """

""" a=[i*2 for i in range(5)]
print(a) """

""" a=[int(i) for i in input().split()]
print(a) """

def name(n):
    n=n.split(" ")
    return n

def summ_spis(a):
    a=name(a)
    s=int(0)
    for i in range(len(a)):
        s+=int(a[i])
        i+=1
    return s
s=input()
print(summ_spis(s))