# [__getattr__(self, name)](https://docs.python.jp/3/reference/datamodel.html#object.__getattr__)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 属性値の検索を行った結果、通常の場所に属性値が見つからなかった場合 (すなわち、 self のインスタンス属性でなく、かつクラスツリーにも見つからなかった場合) に呼び出されます。name は属性名です。このメソッドは (計算された) 属性値を返すか、 AttributeError 例外を送出しなければなりません。

> なお、通常の過程で属性が見つかれば、 __getattr__() は呼び出されません。(これは、 __getattr__() と __setattr__() が意図的に非対称にされている点です。) これは、効率のためと、こうしないと __getattr__() がインスタンスの他の属性値にアクセスする方法がなくなるためです。また、少なくともインスタンス変数に対しては、値をインスタンスの属性値辞書に挿入しないことで (代わりに他のオブジェクトに挿入することで)、属性値を完全に制御しているふりができます。実際に属性アクセスを完全に制御する方法は、以下の __getattribute__() メソッドを参照してください。

## ソースコード

### 試してみた

```python
import datetime
#print(int('100').__getattr__('abcdefg')) # AttributeError: 'int' object has no attribute '__getattr__'
#print(str('abc').__getattr__('abcdefg')) # AttributeError: 'str' object has no attribute '__getattr__'
#print(range(3).__getattr__('abcdefg')) # AttributeError: 'range' object has no attribute '__getattr__'
#print(datetime.datetime.now().__getattr__('abcdefg')) # AttributeError: 'datetime.datetime' object has no attribute '__getattr__'
```
```sh
$ python 0.py 
```

int, str, range, datetimeクラスには実装されていないらしい。

### ユーザ定義クラス

```python
class MyClass:
    def __init__(self, value=0): self.__value = value

s = MyClass()
print(s.__getattr__('abc')) # AttributeError: 'MyClass' object has no attribute '__getattr__'
```
```sh
$ python 1.py 
Traceback (most recent call last):
  File "1.py", line 5, in <module>
    print(s.__getattr__('abc')) # AttributeError: 'MyClass' object has no attribute '__getattr__'
AttributeError: 'MyClass' object has no attribute '__getattr__'
```

ユーザ定義クラスにも実装されていないらしい。

### 実装した

```python
class Blank: pass
class MyClass:
    def __init__(self, value=0): self.__obj = Blank()
    def __getattr__(self, name): getattr(self.__obj, name)
s = MyClass()
print(s.__getattr__('name'))
```
```sh
$ python 2.py 
Traceback (most recent call last):
  File "2.py", line 6, in <module>
    print(s.__getattr__('name'))
  File "2.py", line 4, in __getattr__
    def __getattr__(self, name): getattr(self.__obj, name)
AttributeError: 'Blank' object has no attribute 'name'
```

#### 無限呼出

selfインスタンスを対象にgetattrすると、無限に呼出しされてしまう。

```python
class Blank: pass
class MyClass:
    def __getattr__(self, name): getattr(self, name)
s = MyClass()
print(s.__getattr__('name'))
```
```sh
$ python 3.py 
Traceback (most recent call last):
  File "3.py", line 5, in <module>
    print(s.__getattr__('name'))
  File "3.py", line 3, in __getattr__
    def __getattr__(self, name): getattr(self, name)
  File "3.py", line 3, in __getattr__
    def __getattr__(self, name): getattr(self, name)
  File "3.py", line 3, in __getattr__
    def __getattr__(self, name): getattr(self, name)
  [Previous line repeated 329 more times]
RecursionError: maximum recursion depth exceeded
```
