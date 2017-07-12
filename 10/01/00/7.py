class MetaA(type):
    def __setattr__(cls, name, value):
#        self.__dict__[name] = value
        super(MetaA, cls).__setattr__(name, value)
        print('{}属性に{}を設定しました'.format(name, value))
class A(object, metaclass=MetaA): pass
a = A()
a.attr1 = '123'
A.attr2 = '123456'
