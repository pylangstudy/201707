# [4.4.3. 浮動小数点数に対する追加のメソッド](https://docs.python.jp/3/library/stdtypes.html#additional-methods-on-float)

< [4.4. 数値型 int, float, complex](https://docs.python.jp/3/library/stdtypes.html#numeric-types-int-float-complex) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.4.2. 整数型における追加のメソッド](https://docs.python.jp/3/library/stdtypes.html#additional-methods-on-integer-types)

> 整数型は numbers.Integral 抽象基底クラス (abstract base class) を実装します。さらに、追加のメソッドをいくつか提供します:

* `float.as_integer_ratio()`
* `float.is_integer()`
* `float.hex()`
* `classmethod float.fromhex(s)`

### `float.as_integer_ratio()`

```python
f = 0.5; print(f.as_integer_ratio()) #(1, 2)
f = 0.25; print(f.as_integer_ratio()) # (1, 4)
f = 0.75; print(f.as_integer_ratio()) # (3, 4)
f = 0.2; print(f.as_integer_ratio()) # (3602879701896397, 18014398509481984) (1, 5)にならない
```
```sh
$ python 0.py 
(1, 2)
(1, 4)
(3, 4)
(3602879701896397, 18014398509481984)
```

### `float.is_integer()`

```python
f = 1.0; print(f.is_integer())
f = 1.5; print(f.is_integer())
```
```sh
$ python 1.py 
True
False
```

### `float.hex()`

```python
f = 1.0; print(f.hex())
f = 1.5; print(f.hex())
```
```sh
$ python 2.py 
0x1.0000000000000p+0
0x1.8000000000000p+0
```

### `classmethod float.fromhex(s)`

```python
f = 1.0; print(f.hex(), float.fromhex(str(f.hex())))
f = 1.5; print(f.hex(), float.fromhex(str(f.hex())))
```
```sh
$ python 3.py 
0x1.0000000000000p+0 1.0
0x1.8000000000000p+0 1.5
```

関数名が`from_hex(s)`でないのが気になる。名付けに統一性がないように見える。`int.from_bytes()`, `int.to_bytes()`はアンダーバーがあったのに。

