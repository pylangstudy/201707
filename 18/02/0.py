class Meta(type): pass
class MyClass(metaclass=Meta):
    one = 'one'
    two = 'two'
    def __init__(self):
        self.three = 'three'
        self.four = 'four'

c = MyClass()
print(MyClass.__dict__)
print(c.__dict__)
