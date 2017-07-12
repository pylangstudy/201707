class Human:
    def __init__(self, name='name', age=0):
        self.__name = name
        self.__age = age
    def __format__(self, format_spec):
        if 'name' == format_spec: return self.__name
        elif 'age' == format_spec: return str(self.__age)
        else: return self.__str__()

h = Human()
print('{:name}'.format(h))
print('{:age}'.format(h))
