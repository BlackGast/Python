class cattle():
    bull_id=0
    age=0
    weight=0
    def show(self):
        print(" ", self.bull_id)
        print(" ", self.age)
        print(" ", self.weight)
    def add(self,a,b):
        print(" ", a+b)

#bull1=cattle()
#bull1.bull_id=1
#bull1.age=3
#bull1.weight=85
#bull1.show()
#bull1.add(bull1.age, 5)

class Auto():
    name=""
    color=""
    form=""
    coast=0
    def show(self):
        print(" ", self.color)
        print(" ", self.form)
        print(" ", self.coast)
        print(" ", self.name)

#car1=Auto()
#car1.coast=60000
#car1.color="red"
#car1.form="Cabriolet"
#car1.name="Fer"
#car1.show()

#car2=Auto()
#car2.coast=10000
#car2.color="blue"
#car2.form="Furgon"
#car2.name="Jump"
#car2.show()

''' class Person():
    name=""
    sex=""
    age=0
    weight=0
    height=0
    def show_1_metod(self):
        print(" ", self.name)
        print(" ", self.sex)
        print(" ", self.age)
        print(" ", self.weight)
        print(" ", self.height)
        print("\n")
    def show_2_metod(self):
        print("Привет. Меня зовут ", self.name, ". Рад познокомиться, Константин")
    def show_3_metod(self):
        if int(self.height) < 100:
            print("Карлик")
        elif int(self.height) > 200:
            print("Гигант")
        else:
            print("Среднестатистический человек") '''

''' man=Person()
man.name="Jake"
man.sex="Man"
man.age=25
man.weight=80
man.height=180
man.show_1_metod()
man.show_2_metod()
man.show_3_metod() '''

class Student():
    def __init__(self,name, group, laptop):
        self.name=name
        self.group=group
        self.laptop=laptop
        if laptop ==1:
            self.laptop="Есть"
        else:
            self.laptop="Нет"
        print

#Ann=Student("Аня", "АИБ-19", 1)

class Person():
    def __init__(self, name, sex, age, weight, height):
        self.name=name
        self.sex=sex
        self.age=age
        self.weight=weight
        self.height=height
    def show_1(self):
        print(" ", self.name)
        print(" ", self.sex)
        print(" ", self.age)
        print(" ", self.weight)
        print(" ", self.height)
    def show_2(self):
        print(f"Привет. Меня зовут {self.name}. Рад познокомиться, Константин")
    def show_3(self):
        if int(self.height) < 100:
            print("Карлик")
        elif int(self.height) > 200:
            print("Гигант")
        else:
            print("Среднестатистический человек")

''' man1=Person("Jake", "man", 25, 80, 201)
man1.show_1()
man1.show_2()
man1.show_3() '''

class Pred():
    def __init__(self, text):
        self.text=text
    def show(self):
        print("Lenght: ",len(self.text))
        if [ s for s in self.text if s in '0123456789']:
            print("Есть")
        print(self.text.upper())

p1=Pred("я вижу одну или 1 птицу")
p1.show()