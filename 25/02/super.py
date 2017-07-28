class Base:
    def __init__(self): print('Base.__init__')
class Super(Base):
    def __init__(self):
        super().__init__()
        print('Super.__init__')

s = Super()
