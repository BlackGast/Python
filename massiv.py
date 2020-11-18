from random import randint

N=int(input("столбец"))
M=int(input("col"))
massiv=[]

for i in range(N):
    podmassiv=[]
    for j in range(M):
        podmassiv.append(randint(1, 99))
    massiv.append(podmassiv)

for i in massiv:
    for j in i:
        print(j, end=" ")
    print()

for i in massiv:
    print(i)