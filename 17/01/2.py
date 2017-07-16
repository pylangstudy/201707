class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.name = 'name'
class Super(Base): pass
s = Super()
print(s.name)
print(Super.name)
