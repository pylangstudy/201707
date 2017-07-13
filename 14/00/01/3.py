class Blank: pass
class MyClass:
    def __init__(self): self.__obj = Blank()
    def __getattribute__(self, name): print('__getattribute__', name); return super().__getattribute__(name)
    
s = MyClass()
print(s.__getattribute__('name'))
