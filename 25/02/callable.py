print(callable(1))
print(callable('a'))
print(callable(None))

print()
print(callable(lambda: print('lambda')))
def f(): pass
print(callable(f))

print()
class C: pass
print(callable(C))
print(callable(C()))

print()
class D:
    def __call__(self): pass
print(callable(D))
print(callable(D()))
