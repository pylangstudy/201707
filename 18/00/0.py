class Meta(type): pass
class MyClass(metaclass=Meta): pass
class MySubclass(MyClass): pass
