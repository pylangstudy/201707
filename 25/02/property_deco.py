#class property(fget=None, fset=None, fdel=None, doc=None)
class A:
    def __init__(self): self.__x = None
    @property
    def x(self): print('getx'); return self.__x
    @x.setter
    def x(self, v): print('setx'); self.__x = v
    @x.deleter
    def x(self): print('delx'); del self.__x

a = A()
a.x = 100
print(a.x)
del a.x

# * わかりづらい
#     * getterは@propertyなのにsetter,deleterはgetter名.setterにせねばならない
# * 名前を何度も書かねばならない
#     * 変数名、関数名、アノテーション
#     * `x = { get; set; del; }`のように簡単に実装できないものか
