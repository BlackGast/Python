def string(a):
    print(a) #Выводит строку
    print("Длина строки", len(a)) #Получаем длину строки
    print(a+".") #Проводим операцию сложения с точкой
    if a.find("ре"): #Проверяем, входит ли РЕ в заданную строку
        print("есть 'ре'") 
    else:
        print("нет 'ре'")
    print("Количество 'ре'", a.count("ре")) #Считаем сколько РЕ в строке
    print("Предпоследний символ строки", a[-2]) #Выводим предроследний символ строки
    x = 0
    for i in range(len(a)): #Получаем все символы с нечетными индексами
        if (i%2 != 0):
            print(a[i], end="")
    print()
    print("Количество слов в строке", len(a.split(" "))) #Выводим количество слов в строке

string("Сидел барсук в своей норе и ел картошечку пюре")