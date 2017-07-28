#eval(expression, globals=None, locals=None)
eval('print("ABC")')
a = 100
eval('print(a)', globals(), locals())
