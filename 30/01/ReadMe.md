# [4.3. 比較](https://docs.python.jp/3/library/stdtypes.html#comparisons)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.2. ブール演算 — and, or, not](https://docs.python.jp/3/library/stdtypes.html#boolean-operations-and-or-not)

> Python には 8 種の比較演算があります。比較演算の優先順位は全て同じです (ブール演算より高い優先順位です)。比較は任意に連鎖できます; 例えば、 x < y <= z は x < y and y <= z とほぼ等価ですが、この y は一度だけしか評価されません (どちらにしても、 x < y が偽となれば z は評価されません)。

* `<`,`>`,`=`,`<=`,`>=`,`==`,`!=`,`is`,`is not`
* シーケンス型のみ、`in`, `not in`

## ソースコード

### 確認

```python
print('1 < 2', 1 < 2)
print('2 < 1', 2 < 1)
print('1 < 1', 1 < 1)

print('1 > 2', 1 > 2)
print('2 > 1', 2 > 1)
print('1 > 1', 1 > 1)

print('1 <= 2', 1 <= 2)
print('2 <= 1', 2 <= 1)
print('1 <= 1', 1 <= 1)

print('1 >= 2', 1 >= 2)
print('2 >= 1', 2 >= 1)
print('1 >= 1', 1 >= 1)

print('1 == 2', 1 == 2)
print('2 == 1', 2 == 1)
print('1 == 1', 1 == 1)

print('1 != 2', 1 != 2)
print('2 != 1', 2 != 1)
print('1 != 1', 1 != 1)

print('1 is 1', 1 is 2)
print('1 is 2', 1 is 2)
print('"a" is "a"', "a" is "a")
print('"a" is "b"', "a" is "b")
print('1 is "a"', 1 is "a")

print('2 in [1,2,3]', 2 in [1,2,3])
print('4 in [1,2,3]', 4 in [1,2,3])
```
```sh
$ python 0.py 
1 < 2 True
2 < 1 False
1 < 1 False
1 > 2 False
2 > 1 True
1 > 1 False
1 <= 2 True
2 <= 1 False
1 <= 1 True
1 >= 2 False
2 >= 1 True
1 >= 1 True
1 == 2 False
2 == 1 False
1 == 1 True
1 != 2 True
2 != 1 True
1 != 1 False
1 is 1 False
1 is 2 False
"a" is "a" True
"a" is "b" False
1 is "a" False
2 in [1,2,3] True
4 in [1,2,3] False
```

