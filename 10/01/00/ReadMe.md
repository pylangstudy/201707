# [__new__()](https://docs.python.jp/3/reference/datamodel.html#object.__new__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

* クラス cls の新しいインスタンスを作るために呼び出される
    * 新しいオブジェクトのインスタンスを`return`せねばならない
        * `super(currentclass, cls).__new__(cls[, ...])`に必要な変更を加えたインスタンスを返す
            * cls のインスタンスを返した場合、[__init__()](https://docs.python.jp/3/reference/datamodel.html#object.__init__)が呼び出される
            * cls のインスタンスを返さなかった場合、[__init__()](https://docs.python.jp/3/reference/datamodel.html#object.__init__)は呼び出されない
    * 主な目的は、変更不能な型 (int, str, tuple など) のサブクラスでインスタンス生成をカスタマイズすることにある
    * メタクラスでよくオーバーライドされる
* 静的メソッドである
    * 特別扱いなので明示的に静的メソッドと宣言する必要がない
    * 第一引数`cls`が必要である

## 参考

Python文書は説明不足だしコードもない。理解にはググって外部資料の参照が必要。

* http://www.yunabe.jp/docs/python_metaclass.html
* http://note.crohaco.net/2016/python-metaclass/

## コードを書いて確かめる

### 呼出

__new__でインスタンスを返した時は__init__が実行される。これが正常パターン。すべての型は`object`を継承している。MyClassも同様。`super()`はobjectを指す。

```python
class MyClass:
    def __new__(cls):
        print('__new__')
        return super().__new__(cls)
    def __init__(cls): print('__init__')

c = MyClass()
```
```sh
$ python 0.py 
__new__
__init__
```

以下、イレギュラーな場合では`__init__`が実行されない。

* インスタンスを返さない
* 異なる型のインスタンスを返す

#### インスタンスを返さない

__new__でインスタンスを返さないときは、`__init__`が実行されない。ふつうこのような使い方はしない。無意味。
```python
class MyClass:
    def __new__(cls):  print('__new__')
    def __init__(cls): print('__init__')

c = MyClass()
```
```sh
$ python 1.py 
__new__
```

#### 異なる型のインスタンスを返す

定義したユーザ型と異なる型のインスタンスを返しても`__init__`は実行されない。
```python
class MyClass:
    def __new__(cls, arg):  print('__new__'); return str(arg)
    def __init__(cls): print('__init__')

c = MyClass('abc')
print(c)
```
```sh
$ python 2.py 
__new__
abc
```

## Pythonのクラス

* Pythonのユーザ定義classはobjectを継承している
* Pythonのユーザ定義classはtypeのインスタンスである

上記のような特徴を持っているらしい。

### type

じつは`type()`にてクラス生成ができるらしい。

```python
def func(self, *args, **kwargs): print('func')
MyClass = type('MyClass',
                 (object,),
                 {'attribute1': 'value',
                  'function1': func})
c = MyClass()
c.function1()
print(c.attribute1)
```
```sh
$ python 3.py 
func
value
```

ちなみに、typeの第二引数がタプルでなくリスト`[object]`だと以下のようなエラーになった。

```sh
TypeError: type.__new__() argument 2 must be tuple, not list
```

#### 属性の所属

`attribute1`はインスタンス変数か、クラス変数かを確かめた。以下の結果からインスタンス変数と思われる。

```
def func(self, *args, **kwargs): print('func')
MyClass = type('MyClass',
                 (object,),
                 {'attribute1': 'value',
                  'function1': func})
c1 = MyClass()
print(c1.attribute1)
c2 = MyClass()
c2.attribute1 = 'value2'
print(c1.attribute1)
print(c2.attribute1)
```
```sh
$ python 4.py 
value
value
value2
```

## メタクラス

メタクラスとは、クラスの挙動を制御するための実装をするクラスである。

Python2と3で実装方法が異なる。sixライブラリなるものを使えば共通化できるらしい。[参考](http://note.crohaco.net/2016/python-metaclass/)

* ユーザ定義classはすべてobjectを継承している
* objectはいくつもの関数を持っている。たとえば`__setattr__()`

### ふつうのクラス

ふつうのクラスだと、以下のようにクラス操作でなくインスタンス操作しか実装できない。
```python
class A(object):
    def __setattr__(self, name, value):
        self.__dict__[name] = value
        print('{}属性に{}を設定しました'.format(name, value))
a = A()
a.attr1 = '123'
A.attr2 = '123456'
```
```sh
$ python 6.py 
attr1属性に123を設定しました
```
インスタンス`a`のときは影響しているが、クラス`A`のときは影響していない。そこで、クラス操作を実装するために用いるのがメタクラスである。

### メタクラス

```python
class MetaA(type):
    def __setattr__(cls, name, value):
#        self.__dict__[name] = value
        super(MetaA, cls).__setattr__(name, value)
        print('{}属性に{}を設定しました'.format(name, value))
class A(object, metaclass=MetaA): pass
a = A()
a.attr1 = '123'
A.attr2 = '123456'
```
```sh
$ python 7.py 
attr2属性に123456を設定しました
```

* メタクラスは`type`を継承している
* メタクラス継承クラスは、`class A(object, metaclass=MetaA):`のようにしてobjectとメタクラスを継承している

インスタンス操作には影響しないらしい。

### `__dict__`と`__setattr__()`

__dict__は名前空間の名前辞書。その名前空間がもつすべての属性をもった辞書である。__dict__辞書に代入すれば__setattr__()と雄なじことができる。以下のコードで確認した。

```python
class A(object):
    def __setattr__(self, name, value):
#        self.__dict__[name] = value
        super().__setattr__(name, value)
        print('{}属性に{}を設定しました'.format(name, value))
a = A()
a.attr1 = '123'
A.attr2 = '123456'
print(a.attr1)
```
```sh
$ python 8.py 
attr1属性に123を設定しました
123
```

### メタクラスで何ができるのか

メタクラスの使いどころがわからない。

* [type()](https://docs.python.jp/3/library/functions.html#type)
    * [type-objects](https://docs.python.jp/3/library/stdtypes.html#type-objects)
        * 型オブジェクトには特有の操作はない
        * [types](https://docs.python.jp/3/library/types.html#module-types)モジュール

「型オブジェクトには特有の操作はない」という。`__setattr__`はtypeでなくobjectが持つメソッドなのだろうか？objectとmetaclass=MetaAの2つを継承したときに先述のような動作をするのだろう。つまり「メタクラスはobjectがもつメソッドの操作を変更できる」ということか？

#### 他クラスを変更できるかと思ったができなかった

class`A`の実装をメタクラスで変更できるのではないかと思ったが、できなかった。

```python
class A:
    def func_ins(self): print('func_ins')
#    @classmethod
    def func_cls(cls): print('func_cls')
class MyMeta(type):
    def func_cls(cls):
        print('MyMeta')
        super(MyMeta, cls).func_cls()
class A2(A, metaclass=MyMeta): pass
a = A2()
a.func_ins()
A.func_cls() # TypeError: func_cls() missing 1 required positional argument: 'cls'
```
```sh
$ python 9.py 
func_ins
Traceback (most recent call last):
  File "9.py", line 12, in <module>
    A.func_cls() # TypeError: func_cls() missing 1 required positional argument: 'cls'
TypeError: func_cls() missing 1 required positional argument: 'cls'
```

