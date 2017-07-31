# [4.6.1. 共通のシーケンス演算](https://docs.python.jp/3/library/stdtypes.html#common-sequence-operations)

< [4.6. シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#sequence-types-list-tuple-range) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 

> 以下の表にある演算は、ほとんどのミュータブル、イミュータブル両方のシーケンスでサポートされています。カスタムのシーケンス型にこれらの演算を完全に実装するのが簡単になるように、 collections.abc.Sequence ABC が提供されています。

* [collections.abc.Sequence](https://docs.python.jp/3/library/collections.abc.html#collections.abc.Sequence)

> 以下のテーブルで、シーケンス演算を優先順位が低い順に挙げます。表内で、 s と t は同じ型のシーケンス、 n、 i、 j 、 k は整数、x は s に課された型と値の条件を満たす任意のオブジェクトです。

> in および not in 演算の優先順位は比較演算と同じです。+ (結合) および * (繰り返し)の優先順位は対応する数値演算と同じです。

* `x in s`
* `x not in s`
* `s + t`
* `s * n`
* `s[i]`
* `s[i:j]`
* `s[i:j:k]`
* `len(s)`
* `min(s)`
* `max(s)`
* `s.index(x[, i[, j]])`
* `s.count(x)`

## ソースコード

```python
s = list(range(10))
print(5 in s)
print(5 not in s)
print(s + list(range(11, 20)))
print(s * 2)
print(s[3])
#print(s[1000])#IndexError: list index out of range
print(s[3:7])
print(s[2:9:3])
print(len(s))
print(min(s))
print(max(s))
s0 = list(range(0, 100, 10))
print(s0)
print(s0.count(30))
print(s0.index(30))
print(s0.index(30, 1,2)) #ValueError: 30 is not in list
```
```sh
$ python 0.py 
True
False
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
3
[3, 4, 5, 6]
[2, 5, 8]
10
0
9
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
1
3
Traceback (most recent call last):
  File "0.py", line 16, in <module>
    print(s0.index(30, 1,2)) #ValueError: 30 is not in list
ValueError: 30 is not in list
```

### 文字列に特定の文字列が含まれるか

```python
print("gg" in "eggs")
```
```sh
$ python 1.py 
True
```

### `s * n`の罠

```python
lists = [[]] * 3
print(lists) #[[], [], []]
lists[0].append(3)
print(lists) #[[3], [3], [3]]

lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
print(lists) #[[3], [5], [7]]

lists = [] * 3
print(lists)
lists = [1,2] * 3
print(lists)
```
```sh
$ python 2.py 
[[], [], []]
[[3], [3], [3]]
[[3], [5], [7]]
[]
[1, 2, 1, 2, 1, 2]
```

* [多次元のリストを作るにはどうしますか？](https://docs.python.jp/3/faq/programming.html#faq-multidimensional-list)

### スライス

```python
s = list(range(10))
print(s)
print(s[-1])
print(s[3:1000])
print(s[:3])
print(s[None:3])
print(s[3:None])
print(s[3:])
print(s[3:1])

print(s[2:9:1000])
print(s[2:1000:3])
print(s[1000:9:3])
print(s[2:9:-3])
print(s[2:9:])
print(s[2:9:None])
#print(s[2:9:0]) #ValueError: slice step cannot be zero
print(s[::])
print(s[::2])
print(s[::3])
print(s[::4])
```
```sh
$ python 3.py 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
9
[3, 4, 5, 6, 7, 8, 9]
[0, 1, 2]
[0, 1, 2]
[3, 4, 5, 6, 7, 8, 9]
[3, 4, 5, 6, 7, 8, 9]
[]
[2]
[2, 5, 8]
[]
[]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8]
[0, 3, 6, 9]
[0, 4, 8]
```

### イミュータブルなシーケンスの結合

> イミュータブルなシーケンスの結合は、常に新しいオブジェクトを返します。これは、結合の繰り返しでシーケンスを構築する実行時間コストがシーケンスの長さの合計の二次式になることを意味します。実行時間コストを線形にするには、代わりに以下のいずれかにしてください:

> * str オブジェクトを結合するには、リストを構築して最後に str.join() を使うか、 io.StringIO インスタンスに書き込んで完成してから値を取得してください

> * bytes オブジェクトを結合するなら、同様に bytes.join() や io.BytesIO を使うか、 bytearray オブジェクトでインプレースに結合できます。 bytearray オブジェクトはミュータブルで、効率のいい割り当て超過機構を備えています

> * tuple オブジェクトを結合するなら、代わりに list を拡張してください

> * その他の型については、関連するクラスのドキュメントを調べてください

#### str

```python
print(''.join(['a','b','c']))
print(','.join(['a','b','c']))
#print(str.join(['a','b','c'])) #TypeError: descriptor 'join' requires a 'str' object but received a 'list'

import io
strio = io.StringIO()
for v in ['aaa','b','c']: strio.write(v)
#print(file=strio)
print(strio.getvalue())
strio.close()
```
```sh
$ python 4.py 
abc
a,b,c
aaabc
```

#### byte

```python
s = [b'a', b'b', b'c']
print(s)
#print(bytes.join(s))#TypeError: descriptor 'join' requires a 'bytes' object but received a 'list'
print(b''.join(s))

import io
byteio = io.BytesIO()
for v in s: byteio.write(v)
print(byteio.getvalue())
byteio.close()
```
```sh
$ python 5.py 
[b'a', b'b', b'c']
b'abc'
b'abc'
```

