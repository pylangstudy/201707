class MyClass:
    def __call__(self): print('__call__')

c = MyClass()
c()
c.__call__()

print()
c.__call__ = lambda: print('overriding call')
c()
c.__call__()
