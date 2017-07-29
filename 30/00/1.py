def RetT(): print('True'); return True
def RetF(): print('False'); return False

print('----- or -----')
RetT() or RetF()
RetF() or RetT() #第一引数が偽のときにのみ、第二引数が評価されます。

print('----- and -----')
RetT() and RetF() #第一引数が真のときにのみ、第二引数が評価されます。
RetF() and RetT() #第一引数が真のときにのみ、第二引数が評価されます。

print('----- not -----')
print(not True and True)
print(False or not True)
print(not True == True)
#print(True == not True) #SyntaxError: invalid syntax
print(True == (not True))
