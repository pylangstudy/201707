class MyIterator(object):
    def __init__(self, *numbers):
        self._numbers = numbers
        self._i = 0
        self.__loop_count = 1
        self.__loop_limit = 3
    def __iter__(self): return self
    def __next__(self):
        if self._i == len(self._numbers):
            if self.__loop_limit <= self.__loop_count: raise StopIteration()
            else:
                self.__loop_count += 1
                self._i = 0
        value = self._numbers[self._i]
        self._i += 1
        return value


itr = MyIterator(10, 20, 30)
for num in itr: print('hello %d' % num)
