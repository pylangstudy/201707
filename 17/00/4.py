class Base:
    __slots__ = ['name']
class Super(Base):
    def __init__(self, name='name'): self.name = name

s = Super()
s.__dict__['age'] = 100
print(s.age)
