# [4.6. シーケンス型 — list, tuple, range](https://docs.python.jp/3/library/stdtypes.html#sequence-types-list-tuple-range)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> 基本的なシーケンス型は 3 つあります: リスト、タプル、range オブジェクトです。バイナリデータ や テキスト文字列 を処理するように仕立てられたシーケンス型は、セクションを割いて解説します。

## ソースコード

```python
for v in [1,2,3]: print(v)
for v in (1,2,3): print(v)
for v in range(1,4): print(v)
```
```sh
$ python 0.py 
1
2
3
1
2
3
1
2
3
```

