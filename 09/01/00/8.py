class A(object):
    def __setattr__(self, name, value):
#        self.__dict__[name] = value
        super().__setattr__(name, value)
        print('{}属性に{}を設定しました'.format(name, value))
a = A()
a.attr1 = '123'
A.attr2 = '123456'
print(a.attr1)
