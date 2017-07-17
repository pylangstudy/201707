# [3.3.3.1. Metaclasses](https://docs.python.jp/3/reference/datamodel.html#metaclasses)

< [3.3.3. クラス生成をカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-class-creation) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## クラス生成

> デフォルトでは、クラスは type() を使って構築されます。 クラス本体は新しい名前空間で実行され、クラス名が type(name, bases, namespace) の結果にローカルに束縛されます。

[type()](https://docs.python.jp/3/library/functions.html#type)

### クラス生成のカスタマイズ

> クラス生成プロセスはカスタマイズできます。 そのためにはクラス定義行で metaclass キーワード引数を渡すか、そのような引数を定義行に含む既存のクラスを継承します。 次の例で MyClass と MySubclass は両方とも Meta のインスタンスです:

```python
class Meta(type): pass
class MyClass(metaclass=Meta): pass
class MySubclass(MyClass): pass
```

> クラス定義の中で指定された他のキーワード引数は、後述するすべてのメタクラス操作に渡されます。

> クラス定義が実行される際に、以下のステップが生じます:

>     適切なメタクラスが決定される

>     クラスの名前空間が準備される

>     クラスの本体が実行される

>     クラスオブジェクトが作られる

コード例を行うと何が嬉しいのか？全くわからない。それは放置するとして、メタクラスの作成方法は以下。

* `metaclass`としてtypeを継承したクラスを継承したクラスを作る
    * それを継承したクラスもメタクラスになる

### メタクラス

メタクラスはクラス生成に関する実装を定義するクラス。

#### メタクラスの実装

* [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization)
* [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access)
* [3.3.2.1. デスクリプタ (descriptor) の実装](https://docs.python.jp/3/reference/datamodel.html#implementing-descriptors)

`type`継承クラスに上記で紹介されたメソッドをオーバーライドすることで、クラス生成をカスタマイズできると思われる。`__new__`メソッドなどを使うのだろう。

## ソースコード

まともなコード例がないので、ググって試行錯誤してみた。

* https://docs.python.jp/3/library/functions.html#type
    * https://docs.python.jp/3/library/stdtypes.html#object.__dict__
* https://tarosky.co.jp/tarog/1000

```python
class Meta(type):
#    pass
    def __new__(cls, name, bases, attrs):
        attrs['name'] = 'name'
        return type.__new__(cls, name, bases, attrs);
#    def __new__(cls): return super().__new__();
#    def __new__(cls): super().__init__(); cls.cls_val = 'cls_val'
#    def __init__(self): self.ins_val = 'ins_val'
class MyClass(metaclass=Meta):
    pass
    def __init__(self):
        super().__init__()
        print(MyClass.name, self.name)
#        print(MyClass.cls_val, self.ins_val)

c = MyClass()
```

`attrs`は`__dict__`辞書になるらしい。__dict__はクラスの属性辞書。クラス変数のことだと思う。メタクラスはクラス変数を生成するだけなのか？大して嬉しくない。

__new__メソッドは引数が多すぎるし何をしているのかパッと見わからない。

メタクラスで何ができるのか不明。

#### 簡単に書ける

クラス変数を作成するだけなら、以下のようにふつうに継承したほうが遥かに簡単に書ける。

```python
class Base: cls_val = 'cls_val'
class MyClass(Base): pass

print(MyClass.cls_val)
```

わざわざメタクラスとやらを書く理由が不明。

#### 実行タイミング

`__new__`はいつ実行されるのか？明示的に呼び出していない。なのに、`name`属性ができていた。いつ生成されたのか？以下コードで見た所、`class MyClass(metaclass=Meta):`定義時と思われる。

```python
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['cls_val'] = 'cls_val'
        return type.__new__(cls, name, bases, attrs);
class MyClass(metaclass=Meta): pass

print(MyClass.cls_val)
```

#### もうちょっと楽に書く

`type()`を使わずに書く。__new__はオブジェクトのインスタンスを返せば何でもいいはず。

```python
class Meta(type):
    def __new__(cls, name, bases, attrs):
        cls.cls_val = 'cls_val'
        return cls
class MyClass(metaclass=Meta): pass

print(MyClass.cls_val)
```
```sh
$ python 4.py 
cls_val
```

こんな風に書けるなら、type()を使う理由もわからない。


[__new__()](https://docs.python.jp/3/reference/datamodel.html#object.__new__)は引数`cls`だけで良さそうに見えるのだが、以下エラーになる。Python文書で`object.__new__(cls[, ...])`とあるが、`[, ...]`は任意引数だったはず。

```sh
$ python 4.py 
Traceback (most recent call last):
  File "4.py", line 5, in <module>
    class MyClass(metaclass=Meta): pass
TypeError: __new__() takes 1 positional argument but 4 were given
```

引数が4つ与えられたとある。metaclassとして継承した時はそのような形式になるということか？

複雑というか、暗黙の挙動なのか。やはりふつうに継承したほうが遥かに簡単かつわかりやすい。

