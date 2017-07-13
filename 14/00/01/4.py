class Blank: pass
class MyClass:
    def __init__(self): self.__obj = Blank()
    def __getattr__(self, name): return super().__getattr__(name)
#    def __getattr__(self, name): return getattr(self.__obj, name)
    def __getattribute__(self, name):
        print('__getattribute__', name);
        if hasattr(self, name): print('TRUE'); return super().__getattribute__(name)
        else: print('FALSE'); return self.__getattr__(name)
    
s = MyClass()
print(s.__getattribute__('name'))
