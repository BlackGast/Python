class Pet():

    def __init__(self, name, age, color):
        self.__name=name
        self.age=age
        self.__color=color

    def set(self):
        self.__name=input()
        self.age=input()
        self.__color=input()

    def get(self):
        print(self.__name, self.age, self.__color)

cat=Pet("Vasya", 3, "black")
cat.get()
cat.set()
cat.get()