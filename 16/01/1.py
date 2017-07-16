class Human:
    __slots__ = ['__name', '__age']
    def __init__(self, name='名無し', age=0):
        self.__name = name
        self.__age = age
    @property
    def Name(self): return self.__name
    @property
    def Age(self): return self.__age
c = Human()
print(c)
print(c.Name)
print(c.Age)
c.__dict__['Sex'] = 'F' # AttributeError: 'Human' object has no attribute '__dict__'
