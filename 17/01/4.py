class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.name = 'name'
        print('__init_subclass__')
class Super(Base):
    def __new__(cls): print('__new__'); return super().__new__(cls)
    def __init__(self): print('__init__'); self.age = 0

s = Super()
print(s.name, Super.name)
