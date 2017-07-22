class MyClass:
    def __init__(self, value): self.__value = value
    def __neg__(self): return self.__value * -1;
c = MyClass(100)
print(str(-c))
