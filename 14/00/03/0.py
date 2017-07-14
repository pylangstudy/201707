class MyClass:
    def __init__(self, value=0): self.__value = value; self.name = 'name'
    def __delattr__(self, name):
        print('__delattr__')
        super().__delattr__(name)
s = MyClass()
print(s._MyClass__value)
print(s.name)
#s.__delattr__('_MyClass__value') # AttributeError: 'MyClass' object has no attribute '_MyClass__value'
#s.__delattr__('__value') # AttributeError: __value
s.__delattr__('name')
print(s._MyClass__value)
print(s.name)

