# [4.4.1. 整数型におけるビット単位演算](https://docs.python.jp/3/library/stdtypes.html#bitwise-operations-on-integer-types)

< [4.4. 数値型 int, float, complex](https://docs.python.jp/3/library/stdtypes.html#numeric-types-int-float-complex) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.4.1. 整数型におけるビット単位演算](https://docs.python.jp/3/library/stdtypes.html#bitwise-operations-on-integer

* ビット単位演算は、整数に対してのみ意味があります。
    * 負の数は、その 2 の補数の値として扱われます (演算中にオーバフローが起こらないように十分なビット数があるものと仮定します) 。
* 二項ビット単位演算の優先順位は全て、数値演算よりも低く、比較よりも高くなっています;
    * 単項演算 ~ の優先順位は他の単項数値演算 (+ および -) と同じです。
* 以下の表では、ビット単位演算を優先順位が低い順に並べています:

演算子|説明
------|----
`|`|論理和
`^`|排他的論理和
`&`|論理積
`<<`|左シフト
`>>`|右シフト
`~x`|ビット反転

* シフト系は`pow(2, n)` によるオーバーフローチェックをしないものと等価

```python
print('1, 2, 3 = {0:#b}, {1:#b}, {2:#b}'.format(1, 2, 3))
print('1 | 2 = {}'.format(1 | 2));
print('1 & 2 = {}'.format(1 & 2));
print('1 ^ 3 = {}'.format(1 ^ 3));
print('2<<8 =', 2<<8)
print('255>>2 =', 255>>2)
# short, int, longのように精度制限がないから10進数表記だと符号反転になる
print('~1', ~1, bin(~1))
print('~-1', ~-1, bin(~-1))
print('~2', ~2, bin(~2))
print('~-2', ~-2, bin(~-2))
print('~3', ~3, bin(~3))
print('~-3', ~-3, bin(~-3))

# どうしても左に1が付与される
print('(~3)>>1', (~3)>>1, bin((~3)>>1))
print('(~-3)>>1', (~-3)>>1, bin((~-3)>>1))
print('(~3)<<1', (~3)<<1, bin((~3)<<1))
print('(~-3)<<1', (~-3)<<1, bin((~-3)<<1))
```
```sh
$ python 0.py 
1, 2, 3 = 0b1, 0b10, 0b11
1 | 2 = 3
1 & 2 = 0
1 ^ 3 = 2
2<<8 = 512
255>>2 = 63
~1 -2 -0b10
~-1 0 0b0
~2 -3 -0b11
~-2 1 0b1
~3 -4 -0b100
~-3 2 0b10
(~3)>>1 -2 -0b10
(~-3)>>1 1 0b1
(~3)<<1 -8 -0b1000
(~-3)<<1 4 0b100
```

