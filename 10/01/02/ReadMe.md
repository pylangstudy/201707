# [__del__()](https://docs.python.jp/3/reference/datamodel.html#object.__del__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

* デストラクタとも呼ばれる
* 呼出タイミング
    * インスタンスが消滅させられる際に呼び出される
* 基底と派生の両クラスが`__del__`を持つとき、派生の`__del__`は基底の`__del__`を明示的に呼びださねばならない

### 注釈

* `del x`は`x.__del__()`を直接呼び出さない
    * `x.__del__()`は`x`への参照カウントが 0 になった際にのみ呼び出される
    * `del x`は`x`への参照カウントを 1 つ減らす
        * 参照カウントが0にならない要因
            * 循環参照
            * 例外
                * スタックフレームオブジェクトへの参照 `sys.exc_info()[2]`
                * 対話モードで補足されなかった例外のスタックフレームオブジェクトへの参照 `sys.last_traceback`
        * 対策
            * 循環参照を壊す
            * スタックフレームオブジェクトへの参照を解放する
            * `sys.last_traceback = None`
            * 詳細は[gc](https://docs.python.jp/3/library/gc.html#module-gc)モジュール参照

### 警告

* `__del__()`の実行中に発生した例外は無視される
    * 代わりに`sys.stderr`に警告が出力されます
* モジュールの削除に伴って`__del__()`が呼び出される際
    * グローバル変数はすでに削除済み、または削除中かもしれない
        * 外部の不変関係を維持する上で絶対最低限必要なことだけをすべき

モジュールの削除とは何か？モジュールオブジェクトは`__del__()`関数を持っているということか？「絶対最低限必要なことだけをすべき」の意味がわからない。削除済み変数を2回`del x`したらマズイということだろうか？

* バージョン 1.5 からは、単一のアンダースコアで始まるグローバル変数は、他のグローバル変数が削除される前にモジュールから削除されるよう保証している
    * アンダースコア付きグローバル変数は`__del__()`が呼び出された際、`import`されたモジュールが残っているか確認する上で役立つ

`_x`などの変数は、`_`がないグローバル変数よりも先に削除される。何の意味があるのか不明。importモジュールが残っているか確認とはどういうことか？コードで書いて欲しかった。

## ソースコード

### デストラクタの実装と呼出

```python
class MyClass:
    def __del__(self): print('__del__')
c = MyClass()
```
```sh
$ python3 0.py 
__del__
```

### 継承元デストラクタ呼出

```python
class Base:
    def __del__(self): print('Base.__del__')
class Super(Base):
    def __del__(self): print('Super.__del__'); super().__del__()
c = Super()
```
```sh
$ python3 1.py 
Super__del__
Base.__del__
```

### 継承元デストラクタ呼出

```python
class Base1:
    def __del__(self): print('Base1.__del__')
class Base2:
    def __del__(self): print('Base2.__del__')
class Super(Base1, Base2):
    def __del__(self): print('Super.__del__'); Base2.__del__(self); Base1.__del__(self);
c = Super()
```
```sh
$ python3 2.py 
Super.__del__
Base2.__del__
Base1.__del__
```

### 継承元デストラクタが呼出されない１

```python
class Base:
    def __del__(self): print('Base.__del__')
class Super(Base):
    def __del__(self): print('Super.__del__')
c = Super()
```
```sh
$ python3 3.py 
Super.__del__
```

基底クラスのデストラクタは明示的に呼びださねば実行されない。

### 継承元デストラクタが呼出されない２

```python
class Base1:
    def __del__(self): print('Base1.__del__')
class Base2:
    def __del__(self): print('Base2.__del__')
class Super(Base1, Base2):
    def __del__(self): print('Super.__del__'); super().__del__();
c = Super()
```
```sh
$ python3 4.py 
Super.__del__
Base1.__del__
```

複数ある基底クラスのデストラクタは各自明示的に呼びださねば実行されない。

### delによる削除

```python
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
c1 = MyClass()
del c1
time.sleep(2)
c2 = MyClass()
```
```sh
$ python3 5.py 
MyClass.__del__
MyClass.__del__
```

### スタックトレースによる参照カウント増加

```python
import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
    def method(self): raise Exception()
c = MyClass()
info = None
try: c.method()
except:
    info = sys.exc_info()[2]
    del c
    print(info)
    time.sleep(2)
print(info)
```
```sh
$ python3 6.py 
<traceback object at 0xb70f61e4>
<traceback object at 0xb70f61e4>
MyClass.__del__
```

`del c`実行後2秒間、`MyClass.__del__`が表示されない。参照カウンタが0にならずデストラクタが呼ばれなかったのだろう。その原因が`info = sys.exc_info()[2]`であるというのがPython文書の説明である。

説明どおりであることを確認できた。

#### 対策: スタックフレームオブジェクトへの参照を解放する

期待した結果と違った。

```python
import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
    def method(self): raise Exception()
c = MyClass()
info = None
try: c.method()
except:
    info = sys.exc_info()[2]
    del info
    del c
    time.sleep(2)
```
```sh
$ python3 8.py 
MyClass.__del__
```
`MyClass.__del__`は２秒後に表示された。期待していたのはすぐに表示されること。

cの参照カウンタが0なら`del c`の直後にデストラクタが実行されるはずと期待していたのだが……。

##### `sys.exc_info()[2]`を外して`try-except`文のみ

またしても期待はずれ。

```python
import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
    def method(self): raise Exception()
c = MyClass()
try: c.method()
except: del c; time.sleep(2);
```
```sh
$ python3 8.py 
MyClass.__del__
```

##### `finally`句で`del`

期待通り！

```python
import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
    def method(self): raise Exception()
c = MyClass()
try: c.method()
except: print('except')
finally: del c
time.sleep(2);
```
```sh
$ python3 9.py 
except
MyClass.__del__
```

実行直後に`MyClass.__del__`が表示され、２秒後にプログラムが終了した。期待通り。このことから以下と予想する。

* あるクラスのメソッド内で例外が生じたとき、except句内ではそのクラスの参照カウンタが増加する
    * そのせいで`except`句内で`del c`してもデストラクタが実行されない
* `finally`句ならデストラクタ実行できた

##### `finally`句で`del`

期待通り！

```python
import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
    def method(self): raise Exception()
c = MyClass()
try: c.method()
except: print('except')
finally: c = None
time.sleep(2);
```
```sh
$ python3 A.py 
except
MyClass.__del__
```

実行直後に`MyClass.__del__`が表示され、２秒後にプログラムが終了した。期待通り。このことから以下と予想する。

* あるクラスのメソッド内で例外が生じたとき、except句内ではそのクラスの参照カウンタが増加する
    * そのせいで`except`句内で`del c`してもデストラクタが実行されない
* `finally`句ならデストラクタ実行できた
    * `finally: del c`
    * `finally: c = None`

Module0.py
```python
_gloval_value = '_gloval_value'
gloval_value = 'gloval_value'
```
B.py
```python
#print(dir(locals))
import Module0
#print(dir(locals))
print(Module0._gloval_value)
print(Module0.gloval_value)
del Module0
print(Module0._gloval_value)
print(Module0.gloval_value)
```
```sh
$ python3 B.py 
_gloval_value
gloval_value
Traceback (most recent call last):
  File "B.py", line 7, in <module>
    print(Module0._gloval_value)
NameError: name 'Module0' is not defined
```

Python文書の警告のうち以下の文が理解できない。

> アンダースコア付きグローバル変数は、 __del__() が呼び出された際に、import されたモジュールがまだ残っているか確認する上で役に立ちます。

今回のコードではモジュール名自体が存在しないエラーになっている。アンダースコア付きグローバル変数がどのように役立つのかわからない。

### デストラクタで例外発生

> __del__() の実行中に発生した例外は無視され、代わりに sys.stderr に警告が出力されます。

とある。たしかにプログラムは中断されず最後まで実行された。エラーログはstderrに出力されるらしい。

```python
import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__'); raise Exception('__del__()エラー。')
    def method(self): raise Exception('method()エラー。')
c = MyClass()
try: c.method()
except: print('except')
finally: c = None
time.sleep(2);
print('プログラム実行完了。')
```
```sh
$ python3 C.py 
except
MyClass.__del__
Exception ignored in: <bound method MyClass.__del__ of <__main__.MyClass object at 0xb70acfec>>
Traceback (most recent call last):
  File "C.py", line 4, in __del__
    def __del__(self): print('MyClass.__del__'); raise Exception('__del__()エラー。')
Exception: __del__()エラー。
プログラム実行完了。
```

