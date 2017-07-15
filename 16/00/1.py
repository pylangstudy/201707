class C(object):
    @property
    def x(self):
        return 0

c = C()
c.__dict__['x'] = 1
print(c.x)
c.__dict__['y'] = 1
print(c.y)

