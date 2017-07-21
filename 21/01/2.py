class MyClass:
    def __call__(self):
        print('__call__')
#        super().__call__()
c = MyClass()
c()
