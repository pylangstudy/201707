# [4.2. ブール演算 — and, or, not](https://docs.python.jp/3/library/stdtypes.html#boolean-operations-and-or-not)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.2. ブール演算 — and, or, not](https://docs.python.jp/3/library/stdtypes.html#boolean-operations-and-or-not)

演算子|説明
------|
`x or y`|両者が真のとき真を返す
`x and y`|少なくとも一方が真のとき真を返す
`not x`|反転する

## ソースコード

### 確認

```python
print('----- or -----')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('----- and -----')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('----- not -----')
print(not True)
print(not False)
```
```sh
$ python 0.py 
----- or -----
True
True
True
False
----- and -----
True
False
False
False
----- not -----
False
True
```

### 短絡評価

```python
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
```
```sh
$ python 1.py 
----- or -----
True
False
True
----- and -----
True
False
False
----- not -----
False
False
False
False
```

以下のようになると思っていたのだが。
```sh
----- or -----
True
False
False
True
```
