class Base1:
    def __del__(self): print('Base1.__del__')
class Base2:
    def __del__(self): print('Base2.__del__')
class Super(Base1, Base2):
    def __del__(self): print('Super.__del__'); Base2.__del__(self); Base1.__del__(self);
c = Super()
