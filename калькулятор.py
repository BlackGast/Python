oper=str(input("Введите оператор от 1 до 6: \n1 - сложение, \n2 - вычитание, \n3 - деление, \n4 - умножение, \n5 - возведение в степень, \n6 - остаток от деления \n"))

summ=str("1")
subtract=str("2")
division=str("3")
multiply=str("4")
exp=str("5")
remainder=str("6")

if oper == summ:
    x=int(input("Введите первое число\n"))
    y=int(input("Введите второе число\n"))
    print(x+y)

elif oper == subtract:
    x=int(input("Введите первое число\n"))
    y=int(input("Введите второе число\n"))
    print(x-y)

elif oper == division:
    x=int(input("Введите первое число\n"))
    y=int(input("Введите второе число\n"))
    print(x/y)

elif oper == multiply:
    x=int(input("Введите первое число\n"))
    y=int(input("Введите второе число\n"))
    print(x*y)

elif oper == exp:
    x=int(input("Введите число\n"))
    y=int(input("Введите степень\n"))
    print(x**y)
elif oper == remainder:
    x=int(input("Введите первое число\n"))
    y=int(input("Введите второе число\n"))
    print(x%y)

else:
    pass