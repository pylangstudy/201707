class Base:
    __slots__ = ['name']
    def __init__(self): self.name = 'base_name'
class Super(Base):
    __slots__ = ['name']
    def __init__(self): self.name = 'super_name'

s = Super()
print(s.name)
print(s._Base__name)
