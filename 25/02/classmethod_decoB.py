#!python3.6
#encoding: utf-8
# https://teratail.com/questions/52151
class C:
    def __init__(self): self.value = 'value'
    def __deco(func):
        def wrapper(self, *args, **kwargs):
            print('----- start -----')
            print('self.value =', self.value)
            ret = func(self, *args, **kwargs)
            print('----- end -----')
            return ret
        return wrapper
    @__deco
    def test(self, *args, **kwargs):
        for a in args: print(a)
        for k,v in kwargs.items(): print(k, v)
        return 'RETURN'

print(C().test(1, 'a', key1='value1'))
