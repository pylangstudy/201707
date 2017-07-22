class NumArray:
    def __init__(self):
        self.__values = []
    def __length_hint__(self):
        print('__length_hint__', len(self.__values))
        return len(self.__values)

n = NumArray()
print(len(n)) # TypeError: object of type 'NumArray' has no len()
