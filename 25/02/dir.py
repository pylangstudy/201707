#dir() は主に対話プロンプトでの使用に便利なように提供されている
#厳密性や一貫性を重視して定義された名前のセットというよりも、むしろ興味を引くような名前のセットを返す
print(dir())

class A: pass
print()
print(dir(A))
print()
print(dir(A()))

class B:
    def __dir__(self): return ['BBB']
print()
print(dir(B))
print()
print(dir(B()))
