class Meta(type):
#    def __new__(cls): # TypeError: __new__() takes 1 positional argument but 4 were given
    def __new__(cls, name, bases, attrs):
        cls.cls_val = 'cls_val'
        return cls
class MyClass(metaclass=Meta): pass

print(MyClass.cls_val)
