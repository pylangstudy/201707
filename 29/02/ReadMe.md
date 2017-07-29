# [4.1. 真理値判定](https://docs.python.jp/3/library/stdtypes.html#truth-value-testing)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.1. 真理値判定](https://docs.python.jp/3/library/stdtypes.html#truth-value-testing)

> どのオブジェクトも真理値を判定でき、 if や while 条件に、または以下のブール演算の被演算子に使えます。以下の値は偽と見なされます:

```
* None
* False
* 数値型におけるゼロ。例えば 0, 0.0, 0j 。
* 空のシーケンス。例えば '', (), [] 。
* 空のマッピング。例えば {} 。
```

> ユーザ定義クラスのインスタンスで、そのクラスが __bool__() または __len__() メソッドを定義していれば、それらのメソッドが整数 0 または bool 値 False を返すとき。 [1]

> それ以外の全ての値は真と見なされます — 従って、多くの型のオブジェクトは常に真です。

> ブール値の結果を返す演算および組み込み関数は、特に注釈のない限り常に偽値として 0 または False を返し、真値として 1 または True を返します。 (重要な例外: ブール演算 or および and は常に被演算子のうちの一つを返します。)

## ソースコード

```python
if None: print(None)
if False: print(False)
if 0: print(0)
if 0.0: print(0.0)
if 0j: print(0j)
if {}: print({})
if []: print([])
if (): print(())
if '': print('blank')
if b'': print(b'blank')
```
```sh
$ python 0.py 
```

すべてFalseのため何も表示されない。

