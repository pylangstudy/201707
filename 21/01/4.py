class MyClass: pass
class MyCallable:
    def __call__(self): print('__call__')

print('MyClass', callable(MyClass))
print('MyCallable', callable(MyCallable))
print('MyClass()', callable(MyClass()))
print('MyCallable()', callable(MyCallable()))

