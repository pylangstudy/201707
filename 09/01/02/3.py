class Base:
    def __del__(self): print('Base.__del__')
class Super(Base):
    def __del__(self): print('Super.__del__')
c = Super()
