class Base: pass
class Super(Base):
    __slots__ = ['name']
    def __init__(self, name='name'): self.name = name

s = Super()
s.__dict__['age'] = 100
print(s.age)
