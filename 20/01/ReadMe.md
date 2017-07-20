# [3.3.3.6. メタクラスの例](https://docs.python.jp/3/reference/datamodel.html#metaclass-example)

< [3.3.3. クラス生成をカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-class-creation) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> メタクラスは限りない潜在的利用価値を持っています。これまで試されてきたアイデアには、ログ記録、インタフェースのチェック、自動デリゲーション、自動プロパティ生成、プロキシ、フレームワーク、そして自動リソースロック／同期といったものがあります。

> ここに、 collections.OrderedDict を使い、クラス変数が定義された順序を記憶するメタクラスの例を挙げます:

```python
import collections
class OrderedClass(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()
    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result
class A(metaclass=OrderedClass):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass

print(A.members)
print(A.__dict__)
```
```sh
$ python 0.py 
('__module__', '__qualname__', 'one', 'two', 'three', 'four')
```

> この A のクラス定義が実行されたとき、処理はメタクラスの __prepare__() を呼び出すことから始まり、それは空の collections.OrderedDict を返します。このマッピングは、 A のメソッドと属性を、クラス文の本体内で定義された順に記録します。一旦この定義が実行されると、順序付き辞書は完全に登録され、メタクラスの __new__() メソッドが呼び出されます。このメソッドは新しい型を構築し、順序付き辞書のキーを members と呼ばれる属性に保存します。


* `__prepare__`特殊メソッドは、そのクラスの名前空間用変数をreturnする
* `__new__`特殊メソッドは、そのクラスの型(type)インスタンスをreturnする

## __prepare__がなくても順序を保持していた

```python
import collections
class OrderedClass(type):
    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result
class A(metaclass=OrderedClass):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass

print(A.members)
print(A.__dict__)
```
```sh
$ python 1.py 
('__module__', '__qualname__', 'one', 'two', 'three', 'four')
{'__module__': '__main__', 'one': <function A.one at 0xb71eaa04>, 'two': <function A.two at 0xb71eaa4c>, 'three': <function A.three at 0xb71ea9bc>, 'four': <function A.four at 0xb71ea974>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None, 'members': ('__module__', '__qualname__', 'one', 'two', 'three', 'four')}
```

`__prepare__`特殊メソッドの使いどころがわからない。

