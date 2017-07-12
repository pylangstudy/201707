class MyClass:
    def __new__(cls):
        print('__new__')
        return super().__new__(cls)
    def __init__(cls): print('__init__')

c = MyClass()
