# [3.3.2.1. デスクリプタ (descriptor) の実装](https://docs.python.jp/3/reference/datamodel.html#implementing-descriptors)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下のメソッドは、このメソッドを持つクラス (いわゆる デスクリプタ(descriptor) クラス) のインスタンスが、 オーナー (owner) クラスに存在するときにのみ適用されます

## 一覧

* [__get__(self, instance, owner)](https://github.com/pylangstudy/201707/blob/master/15/00/00/ReadMe.md)
* [__set__(self, instance, value)](https://github.com/pylangstudy/201707/blob/master/15/00/01/ReadMe.md)
* [__delete__(self, instance)](https://github.com/pylangstudy/201707/blob/master/15/00/02/ReadMe.md)
* [__set_name__(self, owner, name)](https://github.com/pylangstudy/201707/blob/master/15/00/03/ReadMe.md)

## __objclass__ 属性

> __objclass__ 属性は inspect モジュールによって解釈され、このオブジェクトが定義されたクラスを特定するのに使われます (この属性を適切に設定しておくと、動的なクラスの属性を実行時に調べる助けになります)。 呼び出される側にとっては、この属性で指定されたクラス (もしくはそのサブクラス) のインスタンスが1番目の位置引数として期待もしくは要求されていることが示せます (例えば、 CPython は束縛されていない C で実行されたメソッドにこの属性を設定します)。

* [inspect](https://docs.python.jp/3/library/inspect.html#module-inspect)

上記リンクで`__objclass__`で文字列検索したが存在しない……。

## __get__の説明

> オーナクラスの属性を取得する (クラス属性へのアクセス) 際や、オーナクラスのインスタンスの属性を取得する (インスタンス属性へのアクセス) 場合に呼び出されます。 owner は常にオーナクラスです。一方、 instance は属性へのアクセスを仲介するインスタンスか属性が owner を介してアクセスされる場合は None になります。このメソッドは (計算された) 属性値を返すか、 AttributeError 例外を送出しなければなりません。

意味不明。以下でググって調べた結果、デスクリプタはプロパティ(getter, setter, deleter)のことらしい。実際に実装するときは`@property`のようにデコレータ形式で実装すると簡単に書けそう。

## 参考

例によってPython文書が意味不明なのでググる。

* http://qiita.com/knzm/items/a8a0fead6e1706663c22
* https://www.ibm.com/developerworks/jp/opensource/library/os-pythondescriptors/index.html
* https://www.python.org/dev/peps/pep-0487/
* http://xaro.hatenablog.jp/entry/2017/01/10/103000

## デスクリプタとは何か

* 管理される属性を作成するための手段である

## デスクリプタで何ができるか

* 属性の値が変更されないように保護する
* 属性の値が変更されたときに依存関係のある別の属性値が自動的に更新されるようにする

## Pythonにおけるデスクリプタ

* Python のデスクリプタは属性を参照した場合に何が起こるかを規定する手段にすぎない
    * 他のプログラミング言語ではgetter,setterと呼ばれる
        * Python にはプライベート変数という概念はない。デスクリプタはプライベート変数に似たものを実現する手段とみなすことができる

## ソースコード

### 第一引数がNoneとインスタンスのときとの違い

```python 
class MyClass:
    cls_val = 'cls_val'
    def __init__(self): self.ins_val = 'ins_val'
    def ins_method(self): return 'cls_method'
    @property
    def prop(self): return 'prop'

c = MyClass()
print(c.ins_val == c.__dict__['ins_val'])

print(MyClass.cls_val == MyClass.__dict__['cls_val'])
print(c.cls_val == MyClass.__dict__['cls_val'])

print(MyClass.__dict__['ins_method'].__get__(None, MyClass))
print(MyClass.__dict__['ins_method'].__get__(c, MyClass))

print(MyClass.__dict__['prop'].__get__(None, MyClass))
print(MyClass.__dict__['prop'].__get__(c, MyClass))
```
```sh
$ python 0.py 
True
True
True
<function MyClass.ins_method at 0xb715c92c>
<bound method MyClass.ins_method of <__main__.MyClass object at 0xb715deec>>
<property object at 0xb70e8374>
prop
```

### 専用クラス

```python
#!python3.6
class Descriptor(object):
    def __init__(self): self._name = None; self._internal_name = None
    def __get__(self, instance, owner):
        print('__get__', self._name)
        return self._name
    def __set__(self, instance, name):
        print('__set__', name)
        self._name = name.title()
    def __delete__(self, instance):
        print('__delete__', self._name)
        del self._name
    def __set_name__(self, owner, name):
        print('__set_name__', owner, name)
        self._name = name
        self._internal_name = '__' + name
class Person(object):
    name = Descriptor()

user = Person()
user.name = 'john smith'
print(user.name)
del user.name
```
```sh
$ python 1.py 
__set_name__ <class '__main__.Person'> name
__set__ john smith
__get__ John Smith
John Smith
__delete__ John Smith
```

1つの属性に対するgetter,setter,deleterをDescriptorという1つのクラスで実装している。

本題から外れるが、`str.title()`という関数を初めて知った。半角スペースで区切られた頭文字を大文字に変換するらしい。

### プロパティ用デコレータ使用

```python
class Person:
    def __init__(self): self._name = ''
    @property
    def Name(self):
        print('getter', self._name)
        return self._name
    @Name.setter
    def Name(self, value):
        print('setter', value)
        self._name = value.title()
    @Name.deleter
    def Name(self):
        print('deleteter', self._name)
        del self._name

user = Person()
user.Name = 'john smith'
print(user.Name)
del user.Name
```
```sh
$ python 2.py 
setter john smith
getter John Smith
John Smith
deleteter John Smith
```

デコレータを使って実装したもの。このほうがスマート。1つのクラスで済む。引数が少ない。ただ、`__set_name__`のデコレータがあるのかどうか知らない。`__set_name__`自体がバージョン 3.6 で追加されたらしいが。

