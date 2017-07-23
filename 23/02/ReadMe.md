# [3.3.9. 特殊メソッド検索](https://docs.python.jp/3/reference/datamodel.html#special-method-lookup)

< [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## 特殊メソッドの暗黙の呼び出し

> カスタムクラスでは、特殊メソッドの暗黙の呼び出しは、オブジェクトのインスタンス辞書ではなく、オブジェクトの型で定義されているときにのみ正しく動作することが保証されます。この動作のため、以下のコードは例外を送出します:

```python
class C: pass
c = C()
c.__len__ = lambda: 5
len(c)
```
```sh
$ python 0.py 
Traceback (most recent call last):
  File "0.py", line 4, in <module>
    len(c)
TypeError: object of type 'C' has no len()
```

### ?

> この動作の背景となる理由は、 __hash__() と __repr__() といった type オブジェクトを含むすべてのオブジェクトで定義されている特殊メソッドにあります。これらのメソッドの暗黙の検索が通常の検索プロセスを使った場合、 type オブジェクト自体に対して実行されたときに失敗してしまいます:

意味不明。

```python
>>> 1 .__hash__() == hash(1)
True
>>> int.__hash__() == hash(int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor '__hash__' of 'int' object needs an argument
```

`1 .__hash__() == hash(1)`は`1 .`のようにスペースがある。スペースががないとエラーになる。謎。

```python
>>> 1.__hash__() == hash(1)
  File "<stdin>", line 1
    1.__hash__() == hash(1)
             ^
SyntaxError: invalid syntax
```

### metaclass confusion

> クラスの非結合メソッドをこのようにして実行しようとすることは、’metaclass confusion’ と呼ばれることもあり、特殊メソッドを検索するときはインスタンスをバイパスすることで回避されます:

```python
>>> type(1).__hash__(1) == hash(1)
True
>>> type(int).__hash__(int) == hash(int)
True
```

クラスのインスタンス参照でも、クラス参照でもなく、`type(instance)`から参照できる、ということか？

### __getattribute__()

> 正確性のためにインスタンス属性をスキップするのに加えて、特殊メソッド検索はオブジェクトのメタクラスを含めて、 __getattribute__() メソッドもバイパスします:

```python
class Meta(type):
    def __getattribute__(*args):
        print("Metaclass getattribute invoked")
        return type.__getattribute__(*args)
class C(object, metaclass=Meta):
    def __len__(self):
        return 10
    def __getattribute__(*args):
        print("Class getattribute invoked")
        return object.__getattribute__(*args)

c = C()
print(c.__len__())                 # Explicit lookup via instance
print(type(c).__len__(c))          # Explicit lookup via type
print(len(c))                      # Implicit lookup
```
```sh
$ python 1.py 
Class getattribute invoked
10
Metaclass getattribute invoked
10
10
```

> このように __getattribute__() 機構をバイパスすることで、特殊メソッドの扱いに関するある程度の自由度と引き換えに (特殊メソッドはインタプリタから一貫して実行されるためにクラスオブジェクトに設定 しなければならない)、インタープリタを高速化するための大きな余地が手に入ります。

意味不明。`__getattribute__(*args)`は第一引数`self`, `cls`がない。インタプリタ高速化と言っていることと関係あるのか？

