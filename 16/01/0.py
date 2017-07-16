class MyClass: pass
c = MyClass()
print(c.__slots__) # AttributeError: 'MyClass' object has no attribute '__slots__'
