class MyClass:
    def __new__(cls): print('__new__'); return super().__new__(cls);
    def __init__(self): print('__init__'); return str('abc');

c = MyClass()
