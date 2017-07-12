# [__bytes__()](https://docs.python.jp/3/reference/datamodel.html#object.__bytes__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> bytes() によって呼び出され、オブジェクトのバイト文字列表現を計算します。これは bytes オブジェクトを返すべきです。

## ソースコード

```python
import datetime
#print(int('100').__bytes__()) # AttributeError: 'int' object has no attribute '__bytes__'
#print(str('abc').__bytes__()) # AttributeError: 'str' object has no attribute '__bytes__'
#print(range(3).__bytes__()) # AttributeError: 'range' object has no attribute '__bytes__
#print(datetime.datetime.now().__bytes__()) # AttributeError: 'datetime.datetime' object has no attribute '__bytes__'
```
```sh
$ python3 0.py 
```

上記の型はどれも__bytes__()を実装していないらしい。バイナリデータ仕様があるデータ型でもないかぎり使うことは無さそう。

