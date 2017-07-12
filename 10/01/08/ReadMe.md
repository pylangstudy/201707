# [__hash__()](https://docs.python.jp/3/reference/datamodel.html#object.__hash__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

* 整数を返さなければならない
* 比較結果が等しいオブジェクトは同じハッシュ値を持たねばならない
    * 要素をタプルに詰めてハッシュ値を計算せよ
* クラスが __eq__() メソッドを定義していないなら、 __hash__() メソッドも定義してはならない
    * ハッシュ可能コレクションの要素として使えない
* クラスがミュータブルなオブジェクトを定義しており、 __eq__() メソッドを実装しているなら、 __hash__() を定義してはならない
    * ハッシュ可能コレクションの実装においてキーのハッシュ値がイミュータブルであることが要求されているから
* ユーザー定義クラスはデフォルトで __eq__() と __hash__() メソッドを持っている

ほか多数の説明がある。しかしそもそも、このhashメソッドを独自実装する理由が何なのかわからない。デフォルトで実装済みらしいし、推奨算出方法まであるのだから独自実装する理由などないように思えるのだが……。イテレーション順序に影響するとあるが、Pythonはこの順序付けを保証しないともある。独自実装する必要性はあるのか？

## ソースコード

```python
class Human:
    def __init__(self, name='name', age=0):
        self.__name = name
        self.__age = age
    def __hash__(self): return hash((self.__name, self.__age))

h0 = Human(name='A', age=0)
h1 = Human(name='A', age=0)
h2 = Human(name='B', age=0)
print(h0.__hash__() == h1.__hash__())
print(h0.__hash__() == h2.__hash__())
```
```sh
$ python3 0.py 
True
False
```

