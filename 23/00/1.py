class MyClass:
    def __init__(self, value): self.__value = value
    def __radd__(self, other): return other + self.__value

c = MyClass(100)
print(23 + c)
print(c + 23)
