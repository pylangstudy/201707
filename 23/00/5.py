class MyClass:
    def __init__(self, value): self.__value = value
    def __int__(self): return int(self.__value)
    def __index__(self):
#        return index(self.__value) # NameError: name 'index' is not defined
        print('__index__')
        return int(self.__value)
c = MyClass(1)
print(int(c))
c = MyClass(1)
print(bin(c))
