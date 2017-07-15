#!python3.6
class Descriptor(object):
    def __init__(self): self._name = None; self._internal_name = None
    def __get__(self, instance, owner):
        print('__get__', self._name)
        return self._name
    def __set__(self, instance, name):
        print('__set__', name)
        self._name = name.title()
    def __delete__(self, instance):
        print('__delete__', self._name)
        del self._name
    def __set_name__(self, owner, name):
        print('__set_name__', owner, name)
        self._name = name
        self._internal_name = '__' + name
class Person(object):
    name = Descriptor()

user = Person()
user.name = 'john smith'
print(user.name)
#print(user._name)
#print(user._Descriptor__name)
print(dir(Person.name))
print(Person.name.__dict__)
del user.name
