class MyClass:
    def __new__(cls):  print('__new__')
    def __init__(cls): print('__init__')

c = MyClass()
