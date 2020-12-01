class Student:
    name="Иван"
    group="АПоб-16"
    skill="Программирование"
    surname="Иванов"
    def set(self, name, surname):
        self.name=name
        self.surname=surname

class Stud_des(Student):
    skill="Дизайн"
    ball=23
#a=Stud_des()
#a.set("Аня", "Иванова")

class Point:
    x1=0
    y1=0

class line(Point):
    x2=0
    y2=0
    
    def lenght(self):
        d=((self.x1-self.x2)**2+(self.y1-self.y2)**2)**0.5
        print(d)

#a=line()
#a.x1=2
#a.x2=3
#a.y1=1
#a.y2=4
#a.lenght()

class Ex:
    def __init__ (self, a, b):
        self.a=a
        self.b=b
    def setS(self):
        print(self.a+self.b)

#p_int=Ex(3,5)
#p_int.setS()
#p_st=Ex("П","а")
#p_st.setS()

#Перегрузка Сложения

class Point:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return Point(self.a+other.a,self.b+other.b)
    def show(self):
        print("(",self.a,";",self.b,")")
#a=Point(3,5)
#b=Point(7,8)
#c=a+b
#c.show()

class drob:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __lt__(self, other):
        if self.a < other.a or self.b < other.b:
            return True
        return False
    def __lt__(self, other):
        if self.a > other.a or self.b > other.b:
            return True
        return False
    def __eq__(self, other):
        if self.a == other.a or self.b == other.b:
            return True
        return False
    def show(self):
        print(self.a, self.b)

a=drob(3,5)
b=drob(7,8)
print(a==b)
print(a < b)
print(a > b)
    
