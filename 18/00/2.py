class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['cls_val'] = 'cls_val'
        return type.__new__(cls, name, bases, attrs);
class MyClass(metaclass=Meta): pass

print(MyClass.cls_val)
