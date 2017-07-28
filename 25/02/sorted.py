#http://akiyoko.hatenablog.jp/entry/2014/09/26/235300
#http://qiita.com/inon3135/items/70b1ed6706579bd48edf
l = [2,1,3,9,0]
print(l)
print(sorted(l))
print(sorted(l, reverse=True))
print(list(reversed(l)))

l = ['1', '2', '123']
print(l)
print(sorted(l))
print(sorted(l, reverse=True))
print(sorted(l, key=lambda x:int(x)))
print(sorted(l, key=lambda x:int(x), reverse=True))

l = [[0, 'Z'], [1, 'Y'], [2, 'X']]
print(l)
print(sorted(l))
print(sorted(l, reverse=True))
print(sorted(l, key=lambda x:x[1]))
print(sorted(l, key=lambda x:x[1], reverse=True))

l = [{'k': 2}, {'k': 3}, {'k': 1}]
print(l)
#print(sorted(l)) # TypeError: '<' not supported between instances of 'dict' and 'dict'
#print(sorted(l, reverse=True)) #TypeError: '<' not supported between instances of 'dict' and 'dict'
print(sorted(l, key=lambda x:x['k']))
print(sorted(l, key=lambda x:x['k'], reverse=True))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#    def __str__(self): return 'name:{} age:{}'.format(self.name, self.age)
    def __repr__(self): return 'name:{} age:{}'.format(self.name, self.age)
l = [Human('B', 3), Human('C', 1), Human('A', 2)]
print(l)
print(sorted(l, key=lambda x:x.name))
print(sorted(l, key=lambda x:x.name, reverse=True))
print(sorted(l, key=lambda x:x.age))
print(sorted(l, key=lambda x:x.age, reverse=True))
