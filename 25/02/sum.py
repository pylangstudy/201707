# sum(iterable[, start])
r = range(11)
l = list(r)
print(l)
print(sum(l))

print(','.join([str(i) for i in l]))

#math.fsum(iterable)
import math
l = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
print(sum(l))
print(math.fsum(l))

#itertools.chain(*iterables)
import itertools
ic = itertools.chain([1,2], [3,4])
print(ic)
for i in ic: print(i)
