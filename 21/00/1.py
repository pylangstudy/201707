from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    def __instancecheck__(self, instance):
        print('__instancecheck__', instance)
        return self.__instancecheck__(instance)
    def __subclasscheck__(self, subclass):
        print('__subclasscheck__', subclass)
        return self.__subclasscheck__(subclass)

assert issubclass(MyABC, MyABC)
assert isinstance(MyABC(), MyABC)
