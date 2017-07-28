#class slice(start, stop[, step])
l = [0,1,2,3,4,5,6,7,8,9]
s = slice(2)
print(s)
print(dir(s))
print(s.start)
print(s.stop)
print(s.step)
print(s.indices)
print(dir(s.indices))
#for i in s.indices: print(i) #TypeError: 'builtin_function_or_method' object is not iterable
s = slice(2,7,3)
print(s)

#itertools.islice(iterable, stop)
#itertools.islice(iterable, start, stop[, step])
import itertools
s = itertools.islice(l, 3)
print(s)
for i in s: print(i)

s = itertools.islice(l, 2, 10, 3)
print(s)
for i in s: print(i)
