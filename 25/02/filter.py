#filter(function, iterable)
l = filter(lambda x: 0 == x % 2, [1,2,3,4])
print(l)
#print(list(l)) #一度参照すると削除されるらしい
for v in l: print(v)
