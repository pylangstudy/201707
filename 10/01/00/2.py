class MyClass:
    def __new__(cls, arg):  print('__new__'); return str(arg)
    def __init__(cls): print('__init__')

c = MyClass('abc')
print(c)
