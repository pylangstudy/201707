class NumArray:
    def __init__(self):
        self.__values = []
    def __len__(self):
        print('__len__', len(self.__values))
        return len(self.__values)

n = NumArray()
print(len(n))
