class MyClass:
    def __init__(self, value=0): self.__value = value

s = MyClass()
print(s._MyClass__value)
s.__setattr__('_MyClass__value', 100)
print(s._MyClass__value)
