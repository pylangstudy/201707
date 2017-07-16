# [3.3.3. クラス生成をカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-class-creation)

< [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> クラスが他のクラスを継承するときに必ず、継承元のクラスの　__init_subclass__ が呼び出されます。これを利用すると、サブクラスの挙動を変更するクラスを書くことができます。これは、クラスデコレータととても良く似ていますが、クラスデコレータが、それが適用された特定のクラスにのみに影響するのに対して、`__init_subclass__`は、もっぱら、このメソッドを定義したクラスの将来のサブクラスに適用されます。

### [classmethod object.__init_subclass__(cls)](https://docs.python.jp/3/reference/datamodel.html#object.__init_subclass__)

> このメソッドは、それが定義されたクラスが継承された際に必ず呼び出されます。cls は新しいサブクラスです。もし、このメソッドがインスタンスメソッドとして定義されると、暗黙的にクラスメソッドに変換されます。

新しいクラスに与えられたキーワード引数は、親のクラスの __init_subclass__ に渡されます。 __init_subclass__ を利用している他のクラスとの互換性のために、以下のコードのように必要なキーワード引数を取得したら、他の引数は基底クラスに引き渡すべきです:

```python
class Philosopher:
    def __init_subclass__(cls, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass
```

> object.__init_subclass__ のデフォルト実装は何も行いませんが、何らかの引数とともに呼び出された場合は、エラーを送出します。

### 注釈

> The metaclass hint metaclass is consumed by the rest of the type machinery, and is never passed to __init_subclass__ implementations. The actual metaclass (rather than the explicit hint) can be accessed as type(cls).

> メタクラスヒントメタクラスは残りのタイプの機械で消費され、__init_subclass__実装には決して渡されません。実際のメタクラス（明示的なヒントではなく）は、型（cls）としてアクセスできます。

Google翻訳してみた。意味不明。メタクラスって何？

> バージョン 3.6 で追加.

## ソースコード

### 継承すると実行される

```python
class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        print('__init_subclass__')
class Super(Base): pass
```
```sh
$ python 1.py 
__init_subclass__
```

`class Super(Base):`のように継承したときに実行される。`s = Super()`のようにコンストラクタ生成せずとも実行される。

### クラス変数を用意させる

```python
class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.name = 'name'
class Super(Base): pass
s = Super()
print(s.name)
print(Super.name)
```
```sh
$ python 2.py 
name
name
```

継承したクラスに`name`というクラス属性を宣言させる。

### __init__

```python
class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.name = 'name'
class Super0(Base): pass
class Super1(Base):
    def __init__(self): self.age = 0

s0 = Super0()
print(s0.name, Super0.name)
s1 = Super1()
print(s1.name, Super1.name, s1.age)
```
```sh
$ python 3.py 
name name
name name 0
```

* 複数クラスがあっても同じように動作する
* 子クラスに__init__があっても動作する

### __new__

```python
class Base:
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.name = 'name'
        print('__init_subclass__')
class Super(Base):
    def __new__(cls): print('__new__'); return super().__new__(cls)
    def __init__(self): print('__init__'); self.age = 0

s = Super()
print(s.name, Super.name)
```
```sh
$ python 4.py 
__init_subclass__
__new__
__init__
name name
```

### __new__と__init_subclass__どちらでもクラス変数生成できる

```python
class Base:
    def __init_subclass__(cls):
        print('__init_subclass__')
        super().__init_subclass__()
        cls.name = 'name'
class Super(Base):
    def __new__(cls): print('__new__'); cls.age = 0; return super().__new__(cls)
    def __init__(self): print('__init__'); self.sex = 'M'

s = Super()
print(s.name, Super.name, s.age, Super.age, s.sex)
#print(Base.name) # AttributeError: type object 'Base' has no attribute 'name'
#print(Base.age) # AttributeError: type object 'Base' has no attribute 'age'
```
```sh
$ python 5.py 
__init_subclass__
__new__
__init__
name name 0 0 M
```

Baseクラスに属性は存在しない。すべてSuperクラスの属性である。__new__はクラス属性を作成し、__init__はインスタンス属性を作成する。__init_subclass__は子クラスのクラス属性を作成する。

## 感想

`__init_subclass__`は使いそうだが、そもそもがややこしい。アクセス修飾子がない(private, public, protectedがない)からややこしくなる。メソッド使い分けの必要まで生じてしまう。

`__init_subclass__`はPython3.6で追加されたらしい。どんどんツギハギになっているような印象。言語仕様がチグハグに見える。全容が把握できない。散らばったチップスの集合として言語仕様になっているように見える。

