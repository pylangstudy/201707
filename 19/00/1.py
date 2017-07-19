code = '''
class MyClass: pass
c = MyClass()
print(c.__class__.__name__)
'''
ret = exec(code, globals(), locals())
print(ret)
c = MyClass()
print(c.__class__.__name__)
