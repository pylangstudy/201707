class MyClass:
    def __init__(self, value): self.__value = value
    def __enter__(self): print('__enter__')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', exc_type, exc_value, traceback)
        if exc_type: return True

with MyClass(100) as c:
    print('in with')
    raise Exception()
