#!python3.6
#encoding: utf-8
# http://www17.atpages.jp/~lambda7/py/decorator.html
def deco1(func):
    def wrapper(*args, **kwargs):
        print('----- deco1 start -----')
        ret = func(*args, **kwargs)
        print('----- deco1 end -----')
        return ret
    return wrapper
def deco2(func):
    def wrapper(*args, **kwargs):
        print('----- deco2 start -----')
        ret = func(*args, **kwargs)
        print('----- deco2 end -----')
        return ret
    return wrapper
@deco1
@deco2
def test(*args, **kwargs):
    for a in args: print(a)
    for k,v in kwargs.items(): print(k, v)
    return 'RETURN'

print(test(1, 'a', key1='value1'))
