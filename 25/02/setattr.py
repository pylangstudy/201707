#setattr(object, name, value)
class C: pass
def A(self): print('method A.')

c = C()
print(dir(c))
setattr(c, 'A', A)
v = 'some value.'
setattr(c, 'value', v)
print(dir(c))
print(c.value)
c.A(c)
