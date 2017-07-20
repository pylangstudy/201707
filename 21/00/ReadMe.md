# [3.3.4. インスタンスのカスタマイズとサブクラスチェック](https://docs.python.jp/3/reference/datamodel.html#customizing-instance-and-subclass-checks)

< [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 以下のメソッドは組み込み関数 isinstance() と issubclass() のデフォルトの動作を上書きするのに利用します。

> 特に、 abc.ABCMeta メタクラスは、抽象基底クラス (ABCs) を”仮想基底クラス (virtual base classes)” として、他の ABC を含む、任意のクラスや (組み込み型を含む) 型に追加するために、これらのメソッドを実装しています。

何の説明もなく現れた[abc.ABCMeta](https://docs.python.jp/3/library/abc.html#abc.ABCMeta)メタクラスとやら。`metaclass=A`と何が違うのか。コード例がないから不明。

> なお、これらのメソッドは、クラスの型 (メタクラス) 上で検索されます。実際のクラスにクラスメソッドとして定義することはできません。これは、インスタンスそれ自体がクラスであるこの場合にのみ、インスタンスに呼び出される特殊メソッドの検索と一貫しています。

「インスタンスそれ自体がクラスである」が意味不明。「クラスインスタンス」を指すのか？`type()`の戻り値のことか？インスタンスという言葉は、クラスからnew(生成)されたオブジェクトのことではないのか？コード例を下さい。

### 参考

[PEP 3119](https://www.python.org/dev/peps/pep-3119) - 抽象基底クラスの導入

抽象基底クラス ([abc](https://docs.python.jp/3/library/abc.html#module-abc) モジュールを参照) を言語に追加する文脈においての動機から、 [__instancecheck__()](https://docs.python.jp/3/reference/datamodel.html#class.__instancecheck__) と [__subclasscheck__()](https://docs.python.jp/3/reference/datamodel.html#class.__subclasscheck__) を通して、 [isinstance()](https://docs.python.jp/3/library/functions.html#isinstance) と [issubclass()](https://docs.python.jp/3/library/functions.html#issubclass) に独自の動作をさせるための仕様の記述があります。

### [class.__instancecheck__(self, instance)](https://docs.python.jp/3/reference/datamodel.html#class.__instancecheck__)

> instance が (直接、または間接的に) class のインスタンスと考えられる場合に true を返します。定義されていれば、 isinstance(instance, class) の実装のために呼び出されます。

### [class.__subclasscheck__(self, subclass)](https://docs.python.jp/3/reference/datamodel.html#class.__subclasscheck__)

> subclass が (直接、または間接的に) class のサブクラスと考えられる場合に true を返します。定義されていれば、 issubclass(subclass, class) の実装のために呼び出されます。

## ソースコード

### [abc.ABCMeta](https://docs.python.jp/3/library/abc.html#abc.ABCMeta)クラス

[abc.ABCMeta](https://docs.python.jp/3/library/abc.html#abc.ABCMeta)を参照してすぐ下にあったコード。

```python
from abc import ABCMeta

class MyABC(metaclass=ABCMeta): pass

MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
```
```sh
$ python 0.py 
```

### 反映されなかった

```python
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    def __instancecheck__(self, instance):
        print('__instancecheck__', instance)
        return self.__instancecheck__(instance)
    def __subclasscheck__(self, subclass):
        print('__subclasscheck__', subclass)
        return self.__subclasscheck__(subclass)

assert issubclass(MyABC, MyABC)
assert isinstance(MyABC(), MyABC)
```
```sh
$ python 1.py 
```

実装の仕方が間違っているのだろうか？コード例を下さい。

### ググった

* http://d.hatena.ne.jp/shomah4a/20110307/1299509176

6年前の個人ブログ様に助けられた。感謝。これによると、Python文書にない情報や、異なっている情報がある。Python3.6.1では何が正しいのか不明。

* `abc.ABCMeta`継承クラスではなく、`type`継承クラスで実装する
    * （そもそもPython文書には一言も書いていないからどう実装すればいいか不明）
* 第一引数は`self`でなく`cls`である
    * （Python文書には`self`とある）

```python
class IterableMeta(type):
    def __instancecheck__(cls, instance):
        print('__instancecheck__', instance)
        return hasattr(instance, '__iter__')
class Iterable(metaclass=IterableMeta): pass

assert isinstance([], Iterable)
```
```sh
$ python 2.py 
__instancecheck__ []
```

## 感想

Python文書が如何にひどいかはっきりした。

Pythonはまるで雲をつかむような学習方法になってしまう。ググって適当なコードをコピペして何となく雰囲気をつかむという方法。

それではきちんとしたコードが書けないから公式文書を見て学習しようとしているのに、個人ブログを見ないと分からないという現実。情報が散らばった上、何が本当か、どのバージョンで使えるのか、謎だらけ。どうしたものか……。

いつかわかりやすくまとめようと思ったが、私には難しそう。違う言語のほうが良いのではないかと思ってしまう。

Python文書はわからない点は適当に流したほうがいいかも。

