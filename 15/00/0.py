class MyClass:
    cls_val = 'cls_val'
    def __init__(self): self.ins_val = 'ins_val'
    def ins_method(self): return 'cls_method'
    @property
    def prop(self): return 'prop'
    """
    def __get__(self, instance, owner):
        print('__get__', instance, owner)
#        super().__get__(self, self.__class__)
        super().__get__(instance, owner)
    """
c = MyClass()
print(c.ins_val == c.__dict__['ins_val'])

print(MyClass.cls_val == MyClass.__dict__['cls_val'])
print(c.cls_val == MyClass.__dict__['cls_val'])

print(MyClass.__dict__['ins_method'].__get__(None, MyClass))
print(MyClass.__dict__['ins_method'].__get__(c, MyClass))

print(MyClass.__dict__['prop'].__get__(None, MyClass))
print(MyClass.__dict__['prop'].__get__(c, MyClass))

