#issubclass(class, classinfo)
class A: pass
print(issubclass(A, object))
print(issubclass(A, A))
class B: pass
print(issubclass(B, A))
class C(A): pass
print(issubclass(C, A))
print(issubclass(C, C))
print(issubclass(C, B))
