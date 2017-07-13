class MyClass:
    def __init__(self, value=0): self.__value = value
    def __setattr__(self, name, value):
        print('__setattr__', name, value)
        super().__setattr__(name, value)
s = MyClass()
print(s._MyClass__value)
s.__setattr__('_MyClass__value', 100)
print(s._MyClass__value)
s._MyClass__value = 123
print(s._MyClass__value)
