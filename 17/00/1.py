class MyClass:
    __slots__ = ['name', '__dict__']
    def __init__(self, name='name'): self.name = name

s = MyClass()
s.__dict__['age'] = 100
print(s.age)
