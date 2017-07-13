class MyClass:
    def __init__(self, value=0): self.__value = value

s = MyClass()
#print(s.__getattribute__('abc')) # AttributeError: 'MyClass' object has no attribute 'abc'
print(s.__getattribute__('__init__')) # AttributeError: 'MyClass' object has no attribute 'abc'
