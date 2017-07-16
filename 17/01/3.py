class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.name = 'name'
class Super0(Base): pass
class Super1(Base):
    def __init__(self): self.age = 0

s0 = Super0()
print(s0.name, Super0.name)
s1 = Super1()
print(s1.name, Super1.name, s1.age)

