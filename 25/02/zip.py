#zip(*iterables)
z = zip([1,2], ['a', 'b'])
print(z)
for i in z: print(i)

z = zip([1,2,3], ['a', 'b'])
print(z)
for i in z: print(i)

#itertools.zip_longest(*iterables, fillvalue=None)
import itertools
iz = itertools.zip_longest([1,2,3], ['a', 'b'])
print(iz)
for i in iz: print(i)

