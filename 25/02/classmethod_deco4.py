#!python3.6
#encoding: utf-8
# http://www17.atpages.jp/~lambda7/py/decorator.html
def deco(func):
    def wrapper(*args, **kwargs): return func(*args, **kwargs)
    return wrapper
@deco
def test(): print('test()'); return 'RETURN'

print(test())
