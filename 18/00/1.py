class Meta(type):
#    pass
    def __new__(cls, name, bases, attrs):
        attrs['name'] = 'name'
        return type.__new__(cls, name, bases, attrs);
#    def __new__(cls): return super().__new__();
#    def __new__(cls): super().__init__(); cls.cls_val = 'cls_val'
#    def __init__(self): self.ins_val = 'ins_val'
class MyClass(metaclass=Meta):
    pass
    def __init__(self):
        super().__init__()
        print(MyClass.name, self.name)
#        print(MyClass.cls_val, self.ins_val)

c = MyClass()
