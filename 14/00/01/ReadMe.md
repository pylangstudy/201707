# [__getattribute__(self, name)](https://docs.python.jp/3/reference/datamodel.html#object.__getattribute__)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> クラスのインスタンスに対する属性アクセスを実装するために、無条件に呼び出されます。クラスが __getattr__() も定義している場合、 __getattr__() は、 __getattribute__() で明示的に呼び出すか、 AttributeError 例外を送出しない限り呼ばれません。このメソッドは (計算された) 属性値を返すか、 AttributeError 例外を送出します。このメソッドが再帰的に際限なく呼び出されてしまうのを防ぐため、実装の際には常に、必要な属性全てへのアクセスで、例えば object.__getattribute__(self, name) のように基底クラスのメソッドを同じ属性名を使って呼び出さなければなりません。

>  言語構文や組み込み関数から暗黙に呼び出された特殊メソッドの検索では、このメソッドも回避されることがあります。 特殊メソッド検索 を参照してください。

[特殊メソッド検索](https://docs.python.jp/3/reference/datamodel.html#special-lookup)

## ソースコード

### 試してみた

```python
import datetime
#print(int('100').__getattribute__('abcdefg')) # AttributeError: 'int' object has no attribute 'abcdefg'
#print(str('abc').__getattribute__('abcdefg')) # AttributeError: 'str' object has no attribute 'abcdefg'
#print(range(3).__getattribute__('abcdefg')) # AttributeError: 'range' object has no attribute 'abcdefg'
#print(datetime.datetime.now().__getattribute__('abcdefg')) # AttributeError: 'datetime.datetime' object has no attribute 'abcdefg'
print(datetime.datetime.now().__getattribute__('now')) # AttributeError: 'datetime.datetime' object has no attribute 'abcdefg'
```
```sh
$ python 0.py 
<built-in method now of type object at 0xb714ffc0>
```

int, str, range, datetimeクラスに実装されているようだ。

### ユーザ定義クラス

```python
class MyClass:
    def __init__(self, value=0): self.__value = value

s = MyClass()
#print(s.__getattribute__('abc')) # AttributeError: 'MyClass' object has no attribute 'abc'
print(s.__getattribute__('__init__')) # AttributeError: 'MyClass' object has no attribute 'abc'
```
```sh
$ python 1.py 
<bound method MyClass.__init__ of <__main__.MyClass object at 0xb71a2d2c>>
```

ユーザ定義クラスにも実装されてるらしい。

### オーバーライドした

```python
class Blank: pass
class MyClass:
    def __init__(self): self.__obj = Blank()
    def __getattribute__(self, name): return getattr(self.__obj, name)
    
s = MyClass()
print(s.__getattribute__('name'))```
```sh
$ python 2.py 
Traceback (most recent call last):
  File "2.py", line 9, in <module>
    print(s.__getattribute__('name'))
  File "2.py", line 6, in __getattribute__
    def __getattribute__(self, name): return getattr(self.__obj, name)
  File "2.py", line 6, in __getattribute__
    def __getattribute__(self, name): return getattr(self.__obj, name)
  File "2.py", line 6, in __getattribute__
    def __getattribute__(self, name): return getattr(self.__obj, name)
  [Previous line repeated 329 more times]
RecursionError: maximum recursion depth exceeded while calling a Python object
```

無限に呼出されてしまった。

### 

```python
class Blank: pass
class MyClass:
    def __init__(self): self.__obj = Blank()
    def __getattribute__(self, name): print('__getattribute__', name); return super().__getattribute__(name)
    
s = MyClass()
print(s.__getattribute__('name'))
```
```sh
$ python 3.py 
__getattribute__ __getattribute__
__getattribute__ name
Traceback (most recent call last):
  File "3.py", line 7, in <module>
    print(s.__getattribute__('name'))
  File "3.py", line 4, in __getattribute__
    def __getattribute__(self, name): print('__getattribute__', name); return super().__getattribute__(name)
AttributeError: 'MyClass' object has no attribute 'name'
```

> 再帰的に際限なく呼び出されてしまうのを防ぐため ... 基底クラスのメソッドを同じ属性名を使って呼び出さなければなりません。

というわけで、親クラスの`__getattribute__`を呼び出すようにした。

### 両方実装した

無限呼出されてしまった。

```python
class Blank: pass
class MyClass:
    def __init__(self): self.__obj = Blank()
    def __getattr__(self, name): return super().__getattr__(name)
#    def __getattr__(self, name): return getattr(self.__obj, name)
    def __getattribute__(self, name):
        print('__getattribute__', name);
        if hasattr(self, name): print('TRUE'); return super().__getattribute__(name)
        else: print('FALSE'); return self.__getattr__(name)
    
s = MyClass()
print(s.__getattribute__('name'))
```
```sh
__getattribute__ __getattribute__
...
Traceback (most recent call last):
  File "4.py", line 12, in <module>
    print(s.__getattribute__('name'))
  File "4.py", line 8, in __getattribute__
    if hasattr(self, name): print('TRUE'); return super().__getattribute__(name)
  File "4.py", line 8, in __getattribute__
    if hasattr(self, name): print('TRUE'); return super().__getattribute__(name)
  File "4.py", line 8, in __getattribute__
    if hasattr(self, name): print('TRUE'); return super().__getattribute__(name)
  [Previous line repeated 328 more times]
  File "4.py", line 7, in __getattribute__
    print('__getattribute__', name);
RecursionError: maximum recursion depth exceeded while calling a Python object
```

## 使いどころ

__getattr__といい、一体何に使うのか。

http://qiita.com/icoxfog417/items/e8f97a6acad07903b5b0#%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AB%E9%9A%A0%E3%81%97%E5%B1%9E%E6%80%A7%E3%81%8C%E5%AD%98%E5%9C%A8%E3%81%99%E3%82%8B

メソッド|説明
--------|----
[__getattr__()](https://docs.python.jp/3/reference/datamodel.html#object.__getattr__)|属性アクセス時、対象属性がなかった場合のみ呼び出される
[__getattribute__()](https://docs.python.jp/3/reference/datamodel.html#object.__getattribute__)|属性アクセス時、常に呼び出される

使い分ける方法もわからない。無限ループになる。

