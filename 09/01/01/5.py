class Base1:
    def __init__(self): print('Base1.__init__');
class Base2:
    def __init__(self): print('Base2.__init__');
class Super(Base1, Base2):
    def __init__(self): print('Super.__init__'); Base1.__init__(self); Base2.__init__(self)

c = Super()
