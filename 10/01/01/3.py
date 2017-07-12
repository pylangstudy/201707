class Base:
    def __init__(self): print('Base.__init__');
class Super(Base):
    def __init__(self): print('Super.__init__'); Base.__init__(self)

c = Super()
