#next(iterator[, default])
#print(next([2,3,1])) #TypeError: 'list' object is not an iterator
itr = iter([2,3,1])
for i in itr: print(i)

i = iter([2,3,1])
print(next(i))
print(next(i))
print(next(i))
print(next(i, None))
#print(next(i)) #StopIteration

m = map(lambda x: x+1, [1,2,3])
print(next(m))
print(next(m))
print(next(m))
print(next(m, None))

f = filter(lambda x: 0 == x % 2, [1,2,3,4])
print(next(f))
print(next(f))
print(next(f, None))

