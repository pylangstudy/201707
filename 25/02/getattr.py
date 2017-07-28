# getattr(object, name[, default])
class C:
    def A(self): pass
print(getattr(C, 'A'))
