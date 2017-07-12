class Human:
    def __init__(self, name='name', age=0): self.__name = name; self.__age = age;
    def __repr__(self): return '{}(name={}, age={})'.format(self.__class__.__name__, self.__name, self.__age)
    def __str__(self): return '{} name:{} age:{}'.format(self.__class__.__name__, self.__name, self.__age)
c = Human(name='Yamada', age=100)
print(c.__repr__())
print(c.__str__())
