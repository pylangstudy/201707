code = '''
def f():
    class MyClass: pass
    c = MyClass()
    print(c.__class__.__name__)
'''
ret = exec(code, globals(), locals())
print(ret)
#c = MyClass() # NameError: name 'MyClass' is not defined
#c = f.MyClass() # AttributeError: 'function' object has no attribute 'MyClass'
#print(c.__class__.__name__)
f()
