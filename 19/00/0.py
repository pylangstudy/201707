def f():
    class MyClass: pass
    c = MyClass()
    print(dir(c))

#c = MyClass() # NameError: name 'MyClass' is not defined
#c = f.MyClass() # AttributeError: 'function' object has no attribute 'MyClass'
f()
