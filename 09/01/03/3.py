class MyClass:
    def __init__(self, value=0): self.__value = value
    def __repr__(self): return '{}({})'.format(self.__class__.__name__, self.__value)
print(MyClass(123).__repr__())
