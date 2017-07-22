class MyClass:
    def __init__(self, value): self.__value = value
    def __add__(self, other): return self.__value + other

c = MyClass(100)
print(c + 23)
print(23 + c)
