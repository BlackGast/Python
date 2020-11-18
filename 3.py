class Point():
    def __init__(self, x, y):
        self.__x=x
        self.__y=y
    def set(self):
        self.__x=int(input("Введите х: "))
        self.__y=int(input("Введите у: "))
    def get(self):
        print("x =", self.__x)
        print("y =", self.__y)

pozition1=Point(1,3)
pozition1.get()
pozition1.set()
pozition1.get()
