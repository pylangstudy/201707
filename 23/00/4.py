class MyClass:
    def __init__(self, value): self.__value = value
    def __int__(self): return int(self.__value)
c = MyClass(1.23)
print(int(c))
