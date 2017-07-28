#isinstance(object, classinfo)
print(isinstance(1, int))
print(isinstance(1, str))
print(isinstance(0.1, float))
print(isinstance('abc', str))
print(isinstance([1,2], list))
print(isinstance((1,2), tuple))
print(isinstance({'k':1}, dict))
print(isinstance(set([1,2]), set))

print()
class A: pass
print(isinstance(A(), object))
print(isinstance(A(), A))
class B: pass
print(isinstance(A(), B))
print(isinstance(B(), A))
print(isinstance(B(), B))

print()
class C(A): pass
print(isinstance(C(), C))
print(isinstance(C(), A))
print(isinstance(C(), B))
print(isinstance(C(), (B, C)))
