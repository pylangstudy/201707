class Blank: pass
class MyClass:
    def __getattr__(self, name): getattr(self, name)
s = MyClass()
print(s.__getattr__('name'))
