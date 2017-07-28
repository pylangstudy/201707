#!python3.6
#encoding: utf-8
# http://www17.atpages.jp/~lambda7/py/decorator.html
def deco(func):
    print('----- start -----')
    func()
    print('----- end -----')
@deco
def test(): print('test()')
