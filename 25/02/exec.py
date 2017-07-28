#exec(object[, globals[, locals]])
exec('print("ABC")')
a = 100
exec('print(a)', globals(), locals())
