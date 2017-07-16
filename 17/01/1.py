class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        print('__init_subclass__')
class Super(Base): pass
