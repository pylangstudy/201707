# [3.3.3.3. クラスの名前空間の準備](https://docs.python.jp/3/reference/datamodel.html#preparing-the-class-namespace)

< [3.3.3. クラス生成をカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-class-creation) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 適切なメタクラスが識別されたら、次にクラスの名前空間が準備されます。メタクラスに __prepare__ 属性がある場合、それは、namespace = metaclass.__prepare__(name, bases, **kwds) として呼ばれます (ここで追加のキーワード引数は、もしあればクラス定義から来ます)。

> If the metaclass has no __prepare__ attribute, then the class namespace is initialised as an empty ordered mapping.

日本語化されていないのでGoogle翻訳した。

> メタクラスに__prepare__属性がない場合、クラスの名前空間は空の順序付きマッピングとして初期化されます。

https://translate.google.co.jp/?hl=ja#en/ja/If%20the%20metaclass%20has%20no%20__prepare__%20attribute%2C%20then%20the%20class%20namespace%20is%20initialised%20as%20an%20empty%20ordered%20mapping.

### 参考

https://www.python.org/dev/peps/pep-3115

> PEP 3115 - Metaclasses in Python 3000

>    __prepare__ 名前空間フックの導入

[Google翻訳](https://translate.google.co.jp/translate?sl=en&tl=ja&js=y&prev=_t&hl=ja&ie=UTF-8&u=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-3115%2F&edit-text=&act=url)

## 解析

「クラスの名前空間」とは、`c.__dict__`辞書のことだろう。メタクラスに__prepare__が実装されていないと「空の順序付きマッピング」になるらしい。何それ？

「空の順序付きマッピング」とはどの型を指しているのか？list, tuple, dict, set, などの型があるが、[collections.OrderedDict](https://docs.python.jp/3/library/collections.html#collections.OrderedDict)のことだろうか？

```python
class Meta(type): pass
class MyClass(metaclass=Meta):
    one = 'one'
    two = 'two'
    def __init__(self):
        self.three = 'three'
        self.four = 'four'

c = MyClass()
print(MyClass.__dict__)
print(c.__dict__)
```
```sh
$ python 0.py 
{'__module__': '__main__', 'one': 'one', 'two': 'two', '__init__': <function MyClass.__init__ at 0xb70f192c>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
{'three': 'three', 'four': 'four'}
```

おそらくソースコードに定義された(上から)順になっている。これが「順序付き」ということだろう。

### 参考

http://qiita.com/pashango2/items/fadc77c8db21c8fd9367

順序付きマッピングで良いのだとしたら、上記のように実装する必要がないのでは？`__prepare__`メソッドは一体何のために実装するのか？

```python
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return collections.OrderedDict()
```

わからないことだらけ。

