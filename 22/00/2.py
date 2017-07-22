class NumArray:
    def __init__(self):
        self.__values = []
    
    def __len__(self):
        print('__len__', len(self.__values))
        return len(self.__values)
    
    def append(self, value):
        self.__check_value(value)
        self.__values.append(value)
    
    def __getitem__(self, key):
        print('__getitem__', key)
        self.__check_key(key)
        return self.__values[key]
    
    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.__check_key(key)
        self.__check_value(value)
        self.__values[key] = value
    
    def __check_key(self, key):
        if not isinstance(key, int): raise TypeError('keyはint型のみ可。:{0}'.format(type(key)))
        if len(self.__values) <= key: raise IndexError('keyが正数のときは0〜{0}の値のみ可。'.format(len(self.__values)-1))
        if key < len(self.__values) * -1: raise IndexError('keyが負数のときは-1〜{0}の値のみ可。'.format(len(self.__values) * -1))
    
    def __check_value(self, value):
        if not isinstance(value, int): raise TypeError('valueはint型のみ可。:{0}'.format(type(value)))
        

n = NumArray()
#n[0] = 0
#n[1] = 100
#n[2] = -100
n.append(0)
n.append(100)
n.append(-100)
print(n)
print(n[0])
print(n[1])
print(n[2])
print(n[-1])
print(n[-2])
print(n[-3])
