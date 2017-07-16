class Human:
    __slots__ = ['__name', '__age']
    def __init__(self, name='名無し', age=0):
        self.__name = name
        self.__age = age
    @property
    def Name(self): return self.__name
    @Name.setter
    def Name(self, value):
        if value: self.__name = value
    @property
    def Age(self): return self.__age
    @Age.setter
    def Age(self, value):
        if 0 <= value: self.__age = value
c = Human()
print(c)
print(c, c.Name, c.Age)
c.Name = '太郎'
c.Age = 10
print(c, c.Name, c.Age)
