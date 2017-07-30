# [4.4.2. 整数型における追加のメソッド](https://docs.python.jp/3/library/stdtypes.html#additional-methods-on-integer-types)

< [4.4. 数値型 int, float, complex](https://docs.python.jp/3/library/stdtypes.html#numeric-types-int-float-complex) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.4.2. 整数型における追加のメソッド](https://docs.python.jp/3/library/stdtypes.html#additional-methods-on-integer-types)

> 整数型は numbers.Integral 抽象基底クラス (abstract base class) を実装します。さらに、追加のメソッドをいくつか提供します:

* `int.bit_length()`
* `int.to_bytes(length, byteorder, *, signed=False)`
* `classmethod int.from_bytes(bytes, byteorder, *, signed=False)`

### `int.bit_length()`

```python
for v in range(10): print(v, bin(v), v.bit_length())
```
```sh
$ python 0.py 
0 0b0 0
1 0b1 1
2 0b10 2
3 0b11 2
4 0b100 3
5 0b101 3
6 0b110 3
7 0b111 3
8 0b1000 4
9 0b1001 4
```


### `int.to_bytes(length, byteorder, *, signed=False)`

```python
for v in range(16): print(v, bin(v), v.to_bytes(1, byteorder='big'), v.to_bytes(1, byteorder='little'))
```
```sh
$ python 1.py 
0 0b0 b'\x00' b'\x00'
1 0b1 b'\x01' b'\x01'
2 0b10 b'\x02' b'\x02'
3 0b11 b'\x03' b'\x03'
4 0b100 b'\x04' b'\x04'
5 0b101 b'\x05' b'\x05'
6 0b110 b'\x06' b'\x06'
7 0b111 b'\x07' b'\x07'
8 0b1000 b'\x08' b'\x08'
9 0b1001 b'\t' b'\t'
10 0b1010 b'\n' b'\n'
11 0b1011 b'\x0b' b'\x0b'
12 0b1100 b'\x0c' b'\x0c'
13 0b1101 b'\r' b'\r'
14 0b1110 b'\x0e' b'\x0e'
15 0b1111 b'\x0f' b'\x0f'
```

### `classmethod int.from_bytes(bytes, byteorder, *, signed=False)`

```python
for v in [v.to_bytes(1, byteorder='big') for v in range(16)]:
    print(v, int.from_bytes(v, byteorder='big'))
```
```sh
$ python 2.py 
b'\x00' 0
b'\x01' 1
b'\x02' 2
b'\x03' 3
b'\x04' 4
b'\x05' 5
b'\x06' 6
b'\x07' 7
b'\x08' 8
b'\t' 9
b'\n' 10
b'\x0b' 11
b'\x0c' 12
b'\r' 13
b'\x0e' 14
b'\x0f' 15
```

