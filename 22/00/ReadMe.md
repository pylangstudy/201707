# [3.3.6. コンテナをエミュレートする](https://docs.python.jp/3/reference/datamodel.html#emulating-container-types)

< [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 以下に挙げるメソッドを定義することで、コンテナオブジェクトを実装できます。コンテナは通常は (リストやタプルのような) シーケンスや (辞書のような) マッピングですが、他のコンテナも同じように表現することができます。最初のメソッド群はシーケンスもしくはマッピングを模倣するために使われます; 両者の違いは、シーケンスでキーとして使えるのは、 N をシーケンスの長さとして 0 <= k < N を満たす整数 k 、もしくは要素の範囲を定義するスライスオブジェクトです。マッピングは、 Python の標準の辞書オブジェクトのメソッドと似た振る舞いをするメソッド keys() 、 values() 、 items() 、 get() 、 clear() 、 setdefault() 、 pop() 、 popitem() 、 copy() 、 update() を提供することも推奨されています。 collections モジュールは、 MutableMapping 抽象基底クラスを提供し、 __getitem__() 、 __setitem__() 、 __delitem__() 、 keys() という基礎となるメソッド群から前文で挙げたメソッドを作成するのを助けてくれます。可変シーケンスは、 Python の標準のリストオブジェクトと同じように、メソッド append() 、 count() 、 index() 、 extend() 、 insert() 、 pop() 、 remove() 、 reverse() 、 sort() を提供すべきです。最後に、シーケンス型は (連結を意味する) 加算と (繰り返しを意味する) 乗算を、以下に説明するメソッド __add__() 、 __radd__() 、 __iadd__() 、 __mul__() 、 __rmul__() 、 __imul__() を定義して実装すべきです; そして、それ以外の数値演算子は定義すべきではありません。マッピングとシーケンスは両方とも、効率の良い in 演算子が使えるように __contains__() メソッドを実装すべきです; マッピングでは in はマッピングのキーを検索すべきです; シーケンスでは値を検索すべきです。マッピングもシーケンスも、コンテナの効率の良い反復処理ができるよう __iter__() メソッドを実装すべきです; マッピングでは __iter__() は keys() と同じであるべきです; シーケンスでは値全体の反復処理を行うべきです。

C#やJavaなら、コレクション型クラスを継承して実装するところだと思う。しかしPython言語では、ユーザ定義クラスに以下のメソッドを継承することでコレクション型を実装するらしい。

### メソッド一覧

メソッド|概要
--------|----
[object.__len__(self)](https://docs.python.jp/3/reference/datamodel.html#object.__len__)|[len()](https://docs.python.jp/3/library/functions.html#len)を実装する。
[object.__length_hint__(self)](https://docs.python.jp/3/reference/datamodel.html#object.__length_hint__)|[operator.length_hint()](https://docs.python.jp/3/library/operator.html#operator.length_hint)を実装する。
[object.__getitem__(self, key)](https://docs.python.jp/3/reference/datamodel.html#object.__getitem__)|`self[key]`を実装する。不正インデクスなら[IndexError](https://docs.python.jp/3/library/exceptions.html#IndexError)、不正キーなら[KeyError](https://docs.python.jp/3/library/exceptions.html#KeyError)を送出すること。
[object.__missing__(self, key)](https://docs.python.jp/3/reference/datamodel.html#object.__missing__)|辞書内にキーが無い場合dict.__getitem__()によって呼び出される。
[object.__setitem__(self, key, value)](https://docs.python.jp/3/reference/datamodel.html#object.__setitem__)|`self[key]`での代入を実装する。
[object.__delitem__(self, key)](https://docs.python.jp/3/reference/datamodel.html#object.__delitem__)|`self[key]`の削除を実装する。
[object.__iter__(self)](https://docs.python.jp/3/reference/datamodel.html#object.__iter__)|コンテナに対してイテレータが要求された際に呼び出される。[イテレータ型](https://docs.python.jp/3/library/stdtypes.html#typeiter)参照。
[object.__reversed__(self)](https://docs.python.jp/3/reference/datamodel.html#object.__reversed__)|[__reversed__()](https://docs.python.jp/3/reference/datamodel.html#object.__reversed__)を実装する。[reversed()](https://docs.python.jp/3/library/functions.html#reversed)より効率の良い実装がある場合のみ実装すべき。
[object.__contains__(self, item)](https://docs.python.jp/3/reference/datamodel.html#object.__contains__)|帰属テスト演算を実装する。`item`が`self`内に存在する場合には真、それ以外は偽を返すべき。[参考](https://docs.python.jp/3/reference/expressions.html#membership-test-details)

## ソースコード

### len

```python
class NumArray:
    def __init__(self):
        self.__values = []
    def __len__(self):
        print('__len__', len(self.__values))
        return len(self.__values)

n = NumArray()
print(len(n))
```
```sh
$ python 0.py 
__len__ 0
0
```

```python
class NumArray:
    def __init__(self):
        self.__values = []
    def __length_hint__(self):
        print('__length_hint__', len(self.__values))
        return len(self.__values)

n = NumArray()
print(len(n))
```
```sh
$ python 1.py 
Traceback (most recent call last):
  File "1.py", line 9, in <module>
    print(len(n))
TypeError: object of type 'NumArray' has no len()
```

`__length_hint__`がいつ、どうやって呼び出されるのか不明。用途も不明。`__len__`と何が違うのか？

### 

```python
class NumArray:
    def __init__(self):
        self.__values = []
    
    def __len__(self):
        print('__len__', len(self.__values))
        return len(self.__values)
    
    def append(self, value):
        self.__check_value(value)
        self.__values.append(value)
    
    def __getitem__(self, key):
        print('__getitem__', key)
        self.__check_key(key)
        return self.__values[key]
    
    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.__check_key(key)
        self.__check_value(value)
        self.__values[key] = value
    
    def __check_key(self, key):
        if not isinstance(key, int): raise TypeError('keyはint型のみ可。:{0}'.format(type(key)))
        if len(self.__values) <= key: raise IndexError('keyが正数のときは0〜{0}の値のみ可。'.format(len(self.__values)-1))
        if key < len(self.__values) * -1: raise IndexError('keyが負数のときは-1〜{0}の値のみ可。'.format(len(self.__values) * -1))
    
    def __check_value(self, value):
        if not isinstance(value, int): raise TypeError('valueはint型のみ可。:{0}'.format(type(value)))
        

n = NumArray()
#n[0] = 0
#n[1] = 100
#n[2] = -100
n.append(0)
n.append(100)
n.append(-100)
print(n)
print(n[0])
print(n[1])
print(n[2])
print(n[-1])
print(n[-2])
print(n[-3])
```
```sh
Traceback (most recent call last):
  File "2.py", line 47, in <module>
    print(n[-4])
  File "2.py", line 15, in __getitem__
    self.__check_key(key)
  File "2.py", line 27, in __check_key
    if key < len(self.__values) * -1: raise IndexError('keyが負数のときは-1〜{0}の値のみ可。'.format(len(self.__values) * -1))
IndexError: keyが負数のときは-1〜-3の値のみ可。
```

コンテナとして利用するには、Python文書の説明にあるとおり、他にもcountなど実装すべきメソッドが多数ある。実装が非常に面倒に思える。

