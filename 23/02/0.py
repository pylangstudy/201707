class C: pass
c = C()
c.__len__ = lambda: 5
len(c)
