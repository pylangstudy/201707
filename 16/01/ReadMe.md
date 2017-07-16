# [3.3.2.3. __slots__](https://docs.python.jp/3/reference/datamodel.html#slots)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下のメソッドは、このメソッドを持つクラス (いわゆる デスクリプタ(descriptor) クラス) のインスタンスが、 オーナー (owner) クラスに存在するときにのみ適用されます

## 参考

http://qiita.com/tma15/items/1d7fbc4d56ac4b3678e1

## Python文書の説明

> デフォルトでは、クラスのインスタンスは属性を保存するための辞書を持っています。これは、ほとんどインスタンス変数を持たないオブジェクトでは領域の無駄です。大量のインスタンスを生成するとき、この記憶領域の消費量は深刻になり得ます。

> このデフォルトの設定は、クラス定義中で __slots__ を定義することでオーバーライドできます。__slots__ 宣言はインスタンス変数のシーケンスを取り、各々のインスタンス上には、各変数の値を記憶するのに必要な量だけの記憶領域を確保します。各々のインスタンスに対して __dict__ が生成されることがないので、記憶領域が節約されます。

ふつうは`__dict__`辞書で属性を保持しているが、__slots__を定義することでメモリ消費を抑えられるらしい。`各変数の値を記憶するのに必要な量だけの記憶領域を確保`するので無駄がないということだろう。

ポイントはメモリ節約でなく「特定の名前しか使えないようにする」ことができることだろう。てっきり`__dict__['new_name'] = 0`でいくらでも自由自在に追加できてしまうと思っていた。しかし`__slots__`をクラス変数として追加すれば、指定した名前しか使えないようにできる。

## ソースコード

### 実装しないと存在しない

```python
class MyClass: pass
c = MyClass()
print(c.__slots__) # AttributeError: 'MyClass' object has no attribute '__slots__'
```

### 実装してみる

クラス変数として`__slots__`を実装する。

```python
class Human:
    __slots__ = ['__name', '__age']
    def __init__(self, name='名無し', age=0):
        self.__name = name
        self.__age = age
    @property
    def Name(self): return self.__name
    @property
    def Age(self): return self.__age
c = Human()
print(c)
print(c.Name)
print(c.Age)
c.__dict__['Sex'] = 'F' # AttributeError: 'Human' object has no attribute '__dict__'
```
```sh
$ python 1.py 
<__main__.Human object at 0xb71beeac>
名無し
0
Traceback (most recent call last):
  File "1.py", line 14, in <module>
    c.__dict__['Sex'] = 'F' # AttributeError: 'Human' object has no attribute '__dict__'
AttributeError: 'Human' object has no attribute '__dict__'
```

`__slots__`を実装すると`__dict__`がなくなるらしい。これで任意の名前しか使えないクラスが作れる。名前を二重定義せねばならない点がダサい。

#### ふつうのクラスは__dict__で追加できる

```python
class Human:
    def __init__(self, name='名無し', age=0):
        self.__name = name
        self.__age = age
    @property
    def Name(self): return self.__name
    @property
    def Age(self): return self.__age
c = Human()
print(c)
print(c.Name)
print(c.Age)
c.__dict__['Sex'] = 'F'
print(c.Sex)
```
```sh
$ python 2.py 
<__main__.Human object at 0xb70f9e8c>
名無し
0
F
```

### setterも実装してみる

```python
class Human:
    __slots__ = ['__name', '__age']
    def __init__(self, name='名無し', age=0):
        self.__name = name
        self.__age = age
    @property
    def Name(self): return self.__name
    @Name.setter
    def Name(self, value):
        if value: self.__name = value
    @property
    def Age(self): return self.__age
    @Age.setter
    def Age(self, value):
        if 0 <= value: self.__age = value
c = Human()
print(c)
print(c, c.Name, c.Age)
c.Name = '太郎'
c.Age = 10
print(c, c.Name, c.Age)
```
```sh
$ python 3.py 
<__main__.Human object at 0xb710af0c>
<__main__.Human object at 0xb710af0c> 名無し 0
<__main__.Human object at 0xb710af0c> 太郎 10
```

同じ名前の定義箇所が多すぎる。名前を変更したくなったとき、変更箇所が多すぎる。修正し忘れが生じてバグの原因になりそう。

* 同じものを意味する別名
    * `__名前`
    * `(頭文字大文字)名前`, 
* 同じものを指す名前の定義箇所
    * __init__の引数
    * __slots__のリスト値
    * `def`名(`@property`, `@名前.setter`, `@名前.deleter`)
    * `@名前.setter`
    * `@名前.deleter`

## 感想

名前を渡しただけでプロパティクラスを作ってくれるようなものが欲しい。たとえば以下みたいに。

```python
cls_type = PropClassMaker.Create('package.module.Class', properties=['name', 'age'])
ins = cls_type('name', 0)
print(ins.Name, ins.Age)
```

できれば、パッケージ、モジュール(ソースコード)も自動作成したい。以下参考。

* https://docs.python.jp/3/library/functions.html#type
* https://docs.python.jp/3/library/types.html
* http://www.lifewithpython.com/2014/12/python-use-eigen-method.html

どうすればいいかわからなかった……。

### C#との比較

C#なら以下のようにスマートに実装できる。

```csharp
class Human {
    public string Name { get; set; }
    public int Age { get; set; }
}
```

こうして比較すると、pythonは見やすいコードではない。短くもない。Pythonコードが如何に冗長で見づらく書きづらいコードであるか鮮明になってしまう。

