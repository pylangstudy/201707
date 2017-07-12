# 比較演算子メソッド

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## 一覧

比較演算子|メソッド名
----------|----------
`<`|[object.__lt__(self, other)](https://docs.python.jp/3/reference/datamodel.html#object.__lt__)
`<=`|[object.__le__(self, other)](https://docs.python.jp/3/reference/datamodel.html#object.__le__)
`==`|[object.__eq__(self, other)](https://docs.python.jp/3/reference/datamodel.html#object.__eq__)
`!=`|[object.__ne__(self, other)](https://docs.python.jp/3/reference/datamodel.html#object.__ne__)
`>`|[object.__gt__(self, other)](https://docs.python.jp/3/reference/datamodel.html#object.__gt__)
`>=`|[object.__ge__(self, other)](https://docs.python.jp/3/reference/datamodel.html#object.__ge__)

## Python文書の説明

* これらはいわゆる “拡張比較 (rich comparison)” メソッドです。
* 拡張比較メソッドは与えられた引数のペアに対する演算を実装していないときに、 シングルトン NotImplemented を返すかもしれません。 慣例として、正常に比較が行われたときには False か True を返します。
* デフォルトでは __ne__() は NotImplemented でない限り __eq__() に委譲して結果を反転させます。
* カスタムの比較演算をサポートしていて、辞書のキーに使うことができるハッシュ可能(hashable) オブジェクトを作るときの重要な注意点について、 __hash__() のドキュメント内に書かれているので参照してください。
* これらのメソッドには (左引数が演算をサポートしないが、右引数はサポートする場合に用いられるような) 引数を入れ替えたバージョンは存在しません。

何を言っているのかさっぱりわからない。ソースコードを書いて欲しい。

## ソースコード

```python
class Class:
    def __init__(self, class_=0): self.__class = class_
    def __str__(self):
        if 0 >= self.__class: return '平社員'
        elif 1 == self.__class: return '部長'
        else: return '社長'
    def __lt__(self, other): return self.__class < other._Class__class

c0 = Class(class_=0)
c1 = Class(class_=1)
c2 = Class(class_=2)
print(c0, c1, c2)
print(c0 < c1)
print(c1 < c0)
```
```sh
$ python3 0.py 
平社員 部長 社長
True
False
```

同様に他のメソッドも実装すれば良さそう。

