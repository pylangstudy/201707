def func(self, *args, **kwargs): print('func')
MyClass = type('MyClass',
                 (object,),
                 {'attribute1': 'value',
                  'function1': func})
c1 = MyClass()
print(c1.attribute1)
c2 = MyClass()
c2.attribute1 = 'value2'
print(c1.attribute1)
print(c2.attribute1)
