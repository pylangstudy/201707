class Base:
    def __init_subclass__(cls):
        print('__init_subclass__')
        super().__init_subclass__()
        cls.name = 'name'
class Super(Base):
    def __new__(cls): print('__new__'); cls.age = 0; return super().__new__(cls)
    def __init__(self): print('__init__'); self.sex = 'M'

s = Super()
print(s.name, Super.name, s.age, Super.age, s.sex)
#print(Base.name) # AttributeError: type object 'Base' has no attribute 'name'
#print(Base.age) # AttributeError: type object 'Base' has no attribute 'age'
