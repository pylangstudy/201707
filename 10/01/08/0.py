class Human:
    def __init__(self, name='name', age=0):
        self.__name = name
        self.__age = age
    def __hash__(self): return hash((self.__name, self.__age))
    def __eq__(self, other): return self.__hash__() == other._Human__hash__()

h0 = Human(name='A', age=0)
h1 = Human(name='A', age=0)
h2 = Human(name='B', age=0)
print(h0.__hash__() == h1.__hash__())
print(h0.__hash__() == h2.__hash__())
