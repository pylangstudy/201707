#min(iterable, *[, key, default])     
#min(arg1, arg2, *args[, key])
print(min(2,3,1))
print(min([2,3,1]))

print(min({'a': 'a', 'A': 'A'}))
print(min({'a': 'a', 'A': 'A'}, key=str.lower, default=None))
print(min({}, key=str.lower, default=None))
print(min({}, key=str.lower, default='default!'))
