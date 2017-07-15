class Person:
    def __init__(self): self._name = ''
    @property
    def Name(self):
        print('getter', self._name)
        return self._name
    @Name.setter
    def Name(self, value):
        print('setter', value)
        self._name = value.title()
    @Name.deleter
    def Name(self):
        print('deleteter', self._name)
        del self._name

user = Person()
user.Name = 'john smith'
print(user.Name)
del user.Name
