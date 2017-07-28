#!python3.6
#encoding: utf-8
# http://www17.atpages.jp/~lambda7/py/decorator.html
def deco(func): print('deco')
@deco
def test(): pass
