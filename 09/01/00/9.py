class A:
    def func_ins(self): print('func_ins')
#    @classmethod
    def func_cls(cls): print('func_cls')
class MyMeta(type):
    def func_cls(cls):
        print('MyMeta')
        super(MyMeta, cls).func_cls()
class A2(A, metaclass=MyMeta): pass
a = A2()
a.func_ins()
A.func_cls() # TypeError: func_cls() missing 1 required positional argument: 'cls'

