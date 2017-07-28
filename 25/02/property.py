#class property(fget=None, fset=None, fdel=None, doc=None)
class A:
    def __init__(self): self.__x = None
    def __getx(self): print('getx'); return self.__x
    def __setx(self, v): print('setx'); self.__x = v
    def __delx(self): print('delx'); del self.__x
    x = property(__getx, __setx, __delx, 'document x.')

a = A()
a.x = 100
print(a.x)
del a.x

# * わかりづらい
#    * クラス定義なのに代入式というのがわかりづらい
