class Pet:
    __Type="Волк"
    __name="Вася"
    age=3
    __color="серый"
    food="говядина"
    height=54

    def set(self, Type, name, age, color, food, height):
        self.__Type=Type
        self.__name=name
        self.age=age
        self.__color=color
        self.food=food
        self.height=height

    def get(self):
        print(self.__Type, self.__name, self.age, self.__color, self.food)
    def __eq__ (self, other):
        if self.__Type == other.__Type or self.food == other.food:
            return True
        return False
    def __add__ (self, other):
        return Pet (self.age + other.age, self.height + other.height)
    def show(self):
        print(self.age, self.height)


class home_Pet(Pet):
    print()
    

dog=Pet()
dog.get()
dog1=home_Pet()
dog1.set("Собака", "Мухтар", 2, "черный", "собачий корм", 65)
dog1.get()
print(dog==dog1)
dog2=home_Pet()
dog2.set("Волк", "Мухтар", 2, "черный", "говядина", 54)
print(dog==dog2)
print(dog+dog1)
dog2.show