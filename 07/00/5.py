class MyClass:
    def __init__(self):
        self.value = 0
a = MyClass()
b = MyClass()
print(a == b)
print(a is b)
print(id(a) == id(b))
print(id(a))
print(id(b))
