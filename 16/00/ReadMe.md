# [3.3.2.2. デスクリプタの呼び出し](https://docs.python.jp/3/reference/datamodel.html#invoking-descriptors)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

> 以下のメソッドは、このメソッドを持つクラス (いわゆる デスクリプタ(descriptor) クラス) のインスタンスが、 オーナー (owner) クラスに存在するときにのみ適用されます

## 一覧

種類|コード例
----|-------
直接呼び出し|`x.__get__(a)`
インスタンス束縛|`a.x`(`type(a).__dict__['x'].__get__(a, type(a))`)
クラス束縛|`A.x`(`A.__dict__['x'].__get__(None, A)`)
super 束縛|`super(B, obj).m()`(`A.__dict__['m'].__get__(obj, obj.__class__)`)

## デスクリプタとは


> デスクリプタとは、特殊な “束縛に関する動作 (binding behaviour)” をもつオブジェクト属性のことです。

> デスクリプタは、デスクリプタプロトコル (descriptor protocol) のメソッド: __get__(), __set__(), および __delete__() を使って、属性アクセスをオーバライドしているものです。

> これらのメソッドのいずれかがオブジェクトに対して定義されている場合、オブジェクトはデスクリプタであるといいます。

以下のコードでいうと、「`Person.name`属性はデスクリプタである」ということだろう。「`Descriptor`クラスはデスクリプタである」と言えるかどうかはわからない。

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
#print(user._name)
#print(user._Descriptor__name)
print(dir(Person.name))
print(Person.name.__dict__)
del user.name
```

## データデスクリプタとは

> デスクリプタが __set__() と __delete__() またはそのどちらかを定義していれば、データデスクリプタとなります

>  もし両方とも定義しなければ、非データデスクリプタです

### オーバーライド

> データデスクリプタは、インスタンス辞書内で属性値が再定義されても、常にこの値をオーバライドします。

> 対照的に、非データデスクリプタの場合には、属性値はインスタンス側でオーバライドされます。

#### メソッド

> (staticmethod() や classmethod() を含む) Python メソッドは、非データデスクリプタとして実装されています。

> その結果、... オーバライドできます。

#### プロパティ

> property() 関数はデータデスクリプタとして実装されています

> 従って、... オーバライドすることができません。


## 参考

* http://qiita.com/knzm/items/a8a0fead6e1706663c22
* http://pyconjp2014-reports.github.io/2014/09/19/01-Python%E3%81%AE%E3%83%87%E3%82%A3%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%82%BF%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/

```python
class C(object):
    @property
    def x(self):
        return 0

c = C()
c.__dict__['x'] = 1
print(c.x)
c.__dict__['y'] = 1
print(c.y)
```

```sh
$ python 1.py 
0
1
```
