class MyClass:
#    name = 'class_attr_name' # ValueError: 'name' in __slots__ conflicts with class variable
    __slots__ = ['name', '__weakref__']
    def __init__(self, name='name'): self.name = name

s = MyClass()
print(s.name)
#print(MyClass.name)
