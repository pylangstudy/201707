#max(iterable, *[, key, default])
#max(arg1, arg2, *args[, key])
print(max(2,3,1))
print(max([2,3,1]))

print(max({'a': 'a', 'A': 'A'}))
print(max({'a': 'a', 'A': 'A'}, key=str.lower, default=None))
print(max({}, key=str.lower, default=None))
print(max({}, key=str.lower, default='default!'))
