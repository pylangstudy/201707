#map(function, iterable, ...)
m = map(lambda x: x+1, [1,2,3])
print(m)
for i in m: print(i)

m = map(lambda x,y: x*y, [1,2,3], [1,2,3])
print(m)
for i in m: print(i)

