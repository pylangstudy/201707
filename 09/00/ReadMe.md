# [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names)

< [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

演算子オーバロードのこと。Python文書の一部が翻訳されていない。

## [__getitem__()](https://docs.python.jp/3/reference/datamodel.html#object.__getitem__)

[__getitem__()](https://docs.python.jp/3/reference/datamodel.html#object.__getitem__)メソッドをオーバーロードしたクラスのインスタンスxは`x[i]`のような操作ができる。`type(x).__getitem__(x, i)`とほぼ等価。

オーバーロードされずに呼び出されたら[AttributeError](https://docs.python.jp/3/library/exceptions.html#AttributeError)か[TypeError](https://docs.python.jp/3/library/exceptions.html#TypeError)になる。

