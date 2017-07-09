def func(self, *args, **kwargs): print('func')
MyClass = type('MyClass',
                 (object,),
                 {'attribute1': 'value',
                  'function1': func})
c = MyClass()
c.function1()
print(c.attribute1)
