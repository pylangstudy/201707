# [3.3.2.3.1. __slots__ を利用する際の注意](https://docs.python.jp/3/reference/datamodel.html#notes-on-using-slots)

< [3.3.2.3. __slots__](https://docs.python.jp/3/reference/datamodel.html#slots) < [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 

    __slots__ を持たないクラスから継承する場合、 __dict__ 属性は常にアクセス可能なので、サブクラスで __slots__ を定義しても意味がありません。


## ソースコード

### 親が__slots__無しなら子で__slots__定義しても意味がない

```python
class Base: pass
class Super(Base):
    __slots__ = ['name']
    def __init__(self, name='name'): self.name = name

s = Super()
s.__dict__['age'] = 100
print(s.age)
```
```sh
$ python 0.py 
100
```

> __slots__ を持たないクラスから継承する場合、 __dict__ 属性は常にアクセス可能なので、サブクラスで __slots__ を定義しても意味がありません。

### __slots__に__dict__を追加して動的追加可にする

```python
class MyClass:
    __slots__ = ['name', '__dict__']
    def __init__(self, name='name'): self.name = name

s = MyClass()
s.__dict__['age'] = 100
print(s.age)
```
```sh
$ python 1.py 
100
```

> __dict__ 変数がない場合、 __slots__ に列挙されていない新たな変数をインスタンスに代入することはできません。列挙されていない変数名を使って代入しようとした場合、 AttributeError が送出されます。新たな変数を動的に代入したいのなら、 __slots__ を宣言する際に '__dict__' を変数名のシーケンスに追加してください。

わざわざ__slots__を宣言する意味があるのか？

### __slots__に__weakref__を追加する

```python
class MyClass:
    __slots__ = ['name', '__weakref__']
    def __init__(self, name='name'): self.name = name

s = MyClass()
print(s.__weakref__)
```
```sh
$ python 2.py 
None
```

> __slots__ を定義しているクラスの各インスタンスに __weakref__ 変数がない場合、インスタンスに対する弱参照 (weak reference) はサポートされません。弱参照のサポートが必要なら、 __slots__ を宣言する際に '__weakref__' を変数名のシーケンスに追加してください。

[弱参照](https://docs.python.jp/3/library/weakref.html)とは、ガーベジコレクションに削除されぬよう保持しておくために使う。

[object.__slots__](https://docs.python.jp/3/reference/datamodel.html#object.__slots__)によると「__dict__ と __weakref__ が自動的に生成されないようにします」らしい。`__weakref__`をどうやって使うのか知らないが、__slots__を宣言した上で欲しいならリストに追加せねばならない。

### __slots__はデスクリプタで実装される

```python
class MyClass:
#    name = 'class_attr_name' # ValueError: 'name' in __slots__ conflicts with class variable
    __slots__ = ['name', '__weakref__']
    def __init__(self, name='name'): self.name = name

s = MyClass()
print(s.name)
#print(MyClass.name)
```
```sh
$ python 3.py 
Traceback (most recent call last):
  File "3.py", line 1, in <module>
    class MyClass:
ValueError: 'name' in __slots__ conflicts with class variable
```

> __slots__ は、クラスのレベルで各変数に対するデスクリプタ (デスクリプタ (descriptor) の実装 を参照) を使って実装されます。その結果、 __slots__ に定義されているインスタンス変数のデフォルト値はクラス属性を使って設定できなくなっています; そうしないと、デスクリプタによる代入をクラス属性が上書きしてしまうからです。

ようするに、__slots__で宣言する名前には、クラス属性の名前と同じものを使えない。

[デスクリプタ (descriptor) の実装](https://docs.python.jp/3/reference/datamodel.html#descriptors)を参照。
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
### __slots__宣言されたクラスのみ対象（継承クラスは対象外）

```python
class Base:
    __slots__ = ['name']
class Super(Base):
    def __init__(self, name='name'): self.name = name

s = Super()
s.__dict__['age'] = 100
print(s.age)
```
```sh
$ python 4.py 
100
```

> __slots__ 宣言が動作するのは、定義が行われたクラスだけに限られています。その結果、サブクラスでは、 __slots__ を定義しない限り __dict__ を持つことになります。

### 


```python
class Base:
    __slots__ = ['name']
    def __init__(self): self.name = 'base_name'
class Super(Base):
    __slots__ = ['name']
    def __init__(self): self.name = 'super_name'

s = Super()
print(s.name)
print(s._Base__name)
```
```sh
$ python 5.py 
super_name
Traceback (most recent call last):
  File "5.py", line 10, in <module>
    print(s._Base__name)
AttributeError: 'Super' object has no attribute '_Base__name'
```

> あるクラスで、基底クラスですでに定義されているスロットを定義した場合、基底クラスのスロットで定義されているインスタンス変数は (デスクリプタを基底クラスから直接取得しない限り) アクセスできなくなります。これにより、プログラムの趣意が不定になってしまいます。将来は、この問題を避けるために何らかのチェックが追加されるかもしれません。

* 「デスクリプタを基底クラスから直接取得」とはどうやるのか？
    * いつもどおり、Python文書にはコード例がないから不明
* 「基底クラスですでに定義されているスロットを定義した場合」とは何か？
    * __slots__変数の宣言を指しているのか？
    * それとも同一の名前を指しているのか？

ようするに現状では「__slots__を宣言したクラスは継承しないほうが無難」ということでいいのか？

### 可変長の組込型から派生したクラスでは使用不可

```python
class NamedInt(int):
    __slots__ = ['name']
    def __init__(self, name='name'): self.name = name

i = NamedInt()
print(i.name)
```
```sh
$ python 6.py 
Traceback (most recent call last):
  File "6.py", line 1, in <module>
    class NamedInt(int):
TypeError: nonempty __slots__ not supported for subtype of 'int'
```

> 空でない __slots__ は、 int や bytes や tuple のような “可変長の” 組み込み型から派生したクラスでは動作しません。

### 

```python
class MyClass0:
    __slots__ = ('name')
    def __init__(self, name='name'): self.name = name
class MyClass1:
    __slots__ = {'name': 'value'}
    def __init__(self, name=None):
        self.name = name if name else MyClass1.__slots__['name']

c0 = MyClass0()
print(c0.name)
c1 = MyClass1()
print(c1.name)
```
```sh
$ python 7.py 
name
value
```

> __slots__ には、文字列でない反復可能オブジェクトを代入することができます。辞書型も使うことができます; しかし将来、辞書の各キーに相当する値に何らかの特殊な意味が割り当てられるかもしれません。

辞書型の場合、値も保持できる。上記コードではデフォルト値として使ってみた。

### __class__へ代入

```python
class MyClass0:
    __slots__ = ('name')
    def __init__(self, name='name'): self.name = name
class MyClass1:
    __slots__ = {'name': 'value'}
    def __init__(self, name=None):
        self.name = name if name else MyClass1.__slots__['name']
class MyClass2:
    __slots__ = ['age']
    def __init__(self, age=0): self.age = age

c0 = MyClass0()
print(c0.name)
c1 = MyClass1()
print(c1.name)
c2 = MyClass2()
print(c2.age)

#c1 = c0
#print(c1.name)
c1.__class__ = c0.__class__
print(c1.name)

#c1 = c2
#print(c1.age)
c1.__class__ = c2.__class__ # TypeError: __class__ assignment: 'MyClass2' object layout differs from 'MyClass0'
print(c1.age)
```
```sh
$ python 8.py 
name
value
0
value
Traceback (most recent call last):
  File "8.py", line 26, in <module>
    c1.__class__ = c2.__class__ # TypeError: __class__ assignment: 'MyClass2' object layout differs from 'MyClass0'
TypeError: __class__ assignment: 'MyClass2' object layout differs from 'MyClass0'
```

> __class__ への代入は、両方のクラスが同じ __slots__ を持っているときのみ動作します。

同じ名前が宣言された__slots__をもつクラス同士は、__class__を代入できる。しかし、異なる__slots__をもつクラスは代入不可。

そもそも、__class__の代入というのが意味不明なのだが……。

