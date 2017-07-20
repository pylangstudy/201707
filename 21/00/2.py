class IterableMeta(type):
    def __instancecheck__(cls, instance):
        print('__instancecheck__', instance)
        return hasattr(instance, '__iter__')
class Iterable(metaclass=IterableMeta): pass

assert isinstance([], Iterable)
