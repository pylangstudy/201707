class MyClass0:
    __slots__ = ('name')
    def __init__(self, name='name'): self.name = name
class MyClass1:
    __slots__ = {'name': 'value'}
    def __init__(self, name=None):
        self.name = name if name else MyClass1.__slots__['name']

c0 = MyClass0()
print(c0.name)
c1 = MyClass1()
print(c1.name)
