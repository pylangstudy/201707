#!python3.6
#encoding: utf-8
# http://www17.atpages.jp/~lambda7/py/decorator.html
def deco(func): return func()
@deco
def test(): print('test()'); return 'A'

test() # TypeError: 'str' object is not callable
