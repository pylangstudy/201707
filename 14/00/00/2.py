class Blank: pass
class MyClass:
    def __init__(self, value=0): self.__obj = Blank()
    def __getattr__(self, name): getattr(self.__obj, name)
s = MyClass()
print(s.__getattr__('name'))
