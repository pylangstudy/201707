class MyClass:
    def __repr__(self): return self.__class__.__name__ + '()'
print(MyClass().__repr__())
