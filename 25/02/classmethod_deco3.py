#!python3.6
#encoding: utf-8
# http://www17.atpages.jp/~lambda7/py/decorator.html
# http://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e
def deco(func):
    def wrapper(): return func()
    return wrapper
@deco
def test(): print('test()'); return 'RETURN'

print(test())
