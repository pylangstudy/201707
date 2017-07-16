class MyClass0:
    __slots__ = ('name')
    def __init__(self, name='name'): self.name = name
class MyClass1:
    __slots__ = {'name': 'value'}
    def __init__(self, name=None):
        self.name = name if name else MyClass1.__slots__['name']
class MyClass2:
    __slots__ = ['age']
    def __init__(self, age=0): self.age = age

c0 = MyClass0()
print(c0.name)
c1 = MyClass1()
print(c1.name)
c2 = MyClass2()
print(c2.age)

#c1 = c0
#print(c1.name)
c1.__class__ = c0.__class__
print(c1.name)

#c1 = c2
#print(c1.age)
c1.__class__ = c2.__class__ # TypeError: __class__ assignment: 'MyClass2' object layout differs from 'MyClass0'
print(c1.age)

