code = '''
def f():
    class MyClass: pass
    c = MyClass()
    print(c.__class__.__name__)
#c = MyClass() # NameError: name 'MyClass' is not defined
#print(c.__class__.__name__)
'''
ret = exec(code, globals(), locals())
print(ret)
f()
