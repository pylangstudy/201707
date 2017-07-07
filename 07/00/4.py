class MyClass: pass
a = MyClass()
b = MyClass()
print(a == b)
print(a is b)
print(id(a) == id(b))
print(id(a))
print(id(b))
