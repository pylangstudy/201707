#!python3.6
#condig:utf-8
#http://qiita.com/Kodaira_/items/42dfe18c81af98bf0db3
#http://momijiame.tumblr.com/post/51805192082/python-superselfclass-self-%E3%81%98%E3%82%83%E3%83%80%E3%83%A1%E3%81%AA%E3%82%93%E3%81%A7%E3%81%99%E3%81%8B
class AppendSuper(type):
    def __new__(cls, name, bases, attrs):
        obj = type.__new__(cls, name, bases, attrs)
        setattr(obj, f'_{name}__super', super(obj))
        return obj

class Base1:
    def __init__(self): print('Base1.__init__')
class Base2:
    def __init__(self): print('Base2.__init__')
class Super(Base1, Base2, metaclass=AppendSuper):
    def __init__(self):
#        print(self.__super)
#        super().__init__() # Base1しか呼べない
#        super(Super).__init__()
#        super(Super, Base2).__init__()
#        super(Base2).__init__()
#        super(Base2, self).__init__()
#        for  c in self.__class__.mro():
#            if not isinstance(c, self.__class__): c.__init__(self) # RecursionError: maximum recursion depth exceeded while calling a Python object
#        Base1.__init__(self) # クラス名を直接指定せねばならない
#        Base2.__init__(self) # クラス名を直接指定せねばならない
        print('Super.__init__')

# super()でBase2.__init__が呼べない…
s = Super()
#print(Super.mro())
