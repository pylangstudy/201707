# [4.5.1. ジェネレータ型](https://docs.python.jp/3/library/stdtypes.html#generator-types)

< [4.5. イテレータ型](https://docs.python.jp/3/library/stdtypes.html#iterator-types) < [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.5.1. ジェネレータ型](https://docs.python.jp/3/library/stdtypes.html#generator-types)

> Python における generator (ジェネレータ) は、イテレータプロトコルを実装する便利な方法を提供します。コンテナオブジェクトの __iter__() メソッドがジェネレータとして実装されていれば、そのメソッドは __iter__() および __next__() メソッドを提供するイテレータオブジェクト (厳密にはジェネレータオブジェクト) を自動的に返します。ジェネレータに関する詳細な情報は、 yield 式のドキュメント にあります。

### 参考

Python文書では実装方法が不明。ググった。

http://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09

## ソースコード

```python
def my_generator():
    yield 1
    yield 2
    yield 3

for v in my_generator(): print(v)
```
```sh
$ python 0.py 
1
2
3
```

