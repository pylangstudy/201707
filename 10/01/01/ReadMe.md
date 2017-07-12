# [__init__()](https://docs.python.jp/3/reference/datamodel.html#object.__init__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

* 呼出タイミング
    * `__new__()`実行後から呼出元に返る前の間に実行される
* 基底と派生の両クラスが`__init__`を持つとき、派生の`__init__`は基底の`__init__`を明示的に呼びださねばならない(`BaseClass.__init__(self, [args...])`)
* `__init__`で非Noneを返してはならない(`TypeError`になる。インスタンス返却は`__new__`に任せる)

## ソースコード

### 非Noneを返してみる

説明どおり`TypeError`になった。

```python
class MyClass:
    def __new__(cls): print('__new__'); return super().__new__(cls);
    def __init__(self): print('__init__'); return super().__new__(MyClass);
        
c = MyClass()
```
```sh
$ python 0.py 
__new__
__init__
Traceback (most recent call last):
  File "0.py", line 5, in <module>
    c = MyClass()
TypeError: __init__() should return None, not 'MyClass'
```

```python
class MyClass:
    def __new__(cls): print('__new__'); return super().__new__(cls);
    def __init__(self): print('__init__'); return str('abc');

c = MyClass()
```
```sh
$ python 1.py 
__new__
__init__
Traceback (most recent call last):
  File "1.py", line 5, in <module>
    c = MyClass()
TypeError: __init__() should return None, not 'str'
```

### 親__init__を呼び出す

#### `super().__init__()`

```python
class Base:
    def __init__(self): print('Base.__init__');
class Super(Base):
    def __init__(self): print('Super.__init__'); super().__init__()

c = Super()
```
```sh
$ python 2.py 
Super.__init__
Base.__init__
```

#### `ClassName.__init__(self)`

```python
class Base:
    def __init__(self): print('Base.__init__');
class Super(Base):
    def __init__(self): print('Super.__init__'); Base.__init__(self)

c = Super()
```
```sh
$ python 3.py 
Super.__init__
Base.__init__
```

#### 親が複数のときに`super().__init__()`

```python
class Base1:
    def __init__(self): print('Base1.__init__');
class Base2:
    def __init__(self): print('Base2.__init__');
class Super(Base1, Base2):
    def __init__(self): print('Super.__init__'); super().__init__()

c = Super()
```
```sh
$ python 4.py 
Super.__init__
Base1.__init__
```

最初の親の分しか実行されない……。

#### 親が複数のときに`ClassName.__init__(self)`

```python
class Base1:
    def __init__(self): print('Base1.__init__');
class Base2:
    def __init__(self): print('Base2.__init__');
class Super(Base1, Base2):
    def __init__(self): print('Super.__init__'); Base1.__init__(self); Base2.__init__(self)

c = Super()
```
```sh
$ python 5.py 
Super.__init__
Base1.__init__
Base2.__init__
```

明示的に呼び出さねば実行されない。ダサい。

* 名前を指定せねばならない
    * 別モジュールを継承する場合、パッケージやモジュール名が変更したらコードを変更せねばならない
        * importするなら名前が重複せぬようにせねばならない
* 第一引数に`self`を与えねばならない

