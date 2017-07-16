class MyClass:
    __slots__ = ['name', '__weakref__']
    def __init__(self, name='name'): self.name = name

s = MyClass()
print(s.__weakref__)
