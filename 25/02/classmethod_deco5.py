#!python3.6
#encoding: utf-8
# http://www17.atpages.jp/~lambda7/py/decorator.html
def deco(func):
    def wrapper(*args, **kwargs): return func(*args, **kwargs)
    return wrapper
@deco
def test(*args, **kwargs):
    for a in args: print(a)
    for k,v in kwargs.items(): print(k, v)
    return 'RETURN'

print(test(1, 'a', key1='value1'))
