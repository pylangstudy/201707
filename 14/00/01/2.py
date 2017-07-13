class Blank: pass
class MyClass:
    def __init__(self): self.__obj = Blank()
#    def __getattr__(self, name): return getattr(self.__obj, name)
#    def __getattribute__(self, name): print('__getattribute__', name); return self.__getattr__(name)
    def __getattribute__(self, name): return getattr(self.__obj, name)
    
s = MyClass()
print(s.__getattribute__('name'))
