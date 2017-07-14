class MyClass:
    def __init__(self, value=0): self.__value = value; self.name = 'name'
    def __dir__(self):
        print('__dir__')
        return super().__dir__()
s = MyClass()
print(dir(s))
