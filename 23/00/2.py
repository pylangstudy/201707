class MyClass:
    def __init__(self, value): self.__value = value
    def __iadd__(self, other): self.__value += other; return self.__value;
c = MyClass(100)
c += 23
print(str(c))
