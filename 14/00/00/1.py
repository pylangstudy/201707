class MyClass:
    def __init__(self, value=0): self.__value = value

s = MyClass()
print(s.__getattr__('abc')) # AttributeError: 'MyClass' object has no attribute '__getattr__'
