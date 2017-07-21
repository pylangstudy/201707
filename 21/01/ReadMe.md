# [3.3.5. 呼び出し可能オブジェクトをエミュレートする](https://docs.python.jp/3/reference/datamodel.html#customizing-instance-and-subclass-checks)

< [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

* [object.__call__(self[, args...])](https://docs.python.jp/3/reference/datamodel.html#object.__call__)

> インスタンスが関数として “呼ばれた” 際に呼び出されます; このメソッドが定義されている場合、 x(arg1, arg2, ...) は x.__call__(arg1, arg2, ...) を短く書いたものになります。

インスタンスとは呼出可能オブジェクトだったのか？コンストラクタのことだろうか？__new__？ __init__？

どうやって”呼び出す”のか？なぜ強調表示？

## ソースコード

### 呼び出されない……

```python
class MyClass:
    def __call__(self):
        print('__call__')
        super().__call__()
c = MyClass()
```
```sh
$ python 0.py 
```

### ググった

http://qiita.com/kyo-bad/items/439d8cc3a0424c45214a

URLでは代入式があるときは実行されていなかった。そこで以下のようにしてみるも、呼び出されない……。

```python
class MyClass:
    def __call__(self):
        print('__call__')
        super().__call__()
MyClass()
```
```sh
$ python 1.py 
```

#### インスタンスに対して実行

http://qiita.com/kyo-bad/items/439d8cc3a0424c45214a

URLではインスタンス変数に対して呼出形式を使っていたときに呼び出されているように見えた。

```python
class MyClass:
    def __call__(self):
        print('__call__')
#        super().__call__() # AttributeError: 'super' object has no attribute '__call__'
c = MyClass()
c()
```
```sh
$ python 2.py 
__call__
```

実行された。Pythonはインスタンスを関数形式で呼び出せるらしい。なにこれ。関数でもコンストラクタでもない。どんな用途に使うのか？初期化とか？ふつうはメソッド名がないと意味不明になりそう。

### a()とa.__call__()は等価ではない

http://qiita.com/myuon_myon/items/8cfd7706120ef3130513

感謝。

```python
class MyClass:
    def __call__(self): print('__call__')

c = MyClass()
c()
c.__call__()

print()
c.__call__ = lambda: print('overriding call')
c()
c.__call__()
```
```sh
$ python 3.py 
__call__
__call__

__call__
overriding call
```

`c.__call__`に新たな関数を代入しても、`c()`で実行されない。つまり、c.__call__と、c()は別の関数であるということ。

Python文書には書いていない情報。

### __call__をオーバーライドしたクラスのインスタンスはcallable()=Trueになる

http://atasatamatara.hatenablog.jp/entry/20120817/1345162948

感謝。

```python
class MyClass: pass
class MyCallable:
    def __call__(self): print('__call__')

print('MyClass', callable(MyClass))
print('MyCallable', callable(MyCallable))
print('MyClass()', callable(MyClass()))
print('MyCallable()', callable(MyCallable()))
```
```sh
$ python 4.py 
MyClass True
MyCallable True
MyClass() False
MyCallable() True
```

クラスはすべてcallable。インスタンスは、__call__をオーバーライドしたクラスのみ、callable。

Python文書にはない情報。

で、__call__の使いどころは？余計な機能ばかりが多くて、コードに書いたらわかりづらくなりそう。


