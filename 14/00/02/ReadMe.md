# [__setattr__(self, name)](https://docs.python.jp/3/reference/datamodel.html#object.__setattr__)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 属性の代入が試みられた際に呼び出されます。これは通常の代入の過程 (すなわち、インスタンス辞書への値の代入) の代わりに呼び出されます。name は属性名で、value はその属性に代入する値です。

> __setattr__() の中でインスタンス属性への代入が必要なら、基底クラスのこれと同じ名前のメソッドを呼び出さなければなりません。例えば、 object.__setattr__(self, name, value) とします。

## ソースコード

### 試してみた

```python
import datetime
#print(int('100').__setattr__('abcdefg', 0)) # AttributeError: 'int' object has no attribute 'abcdefg'
#print(str('abc').__setattr__('abcdefg', 'value')) # AttributeError: 'str' object has no attribute 'abcdefg'
#print(range(3).__setattr__('abcdefg', 'value')) # AttributeError: 'range' object has no attribute 'abcdefg'
#print(datetime.datetime.now().__setattr__('abcdefg', 'value')) # AttributeError: 'datetime.datetime' object has no attribute 'abcdefg'
#print(datetime.datetime.now().__setattr__('now', 'value')) # AttributeError: 'datetime.datetime' object attribute 'now' is read-only
```
```sh
$ python 0.py 
```

AttributeError。__setattr__で代入する前に__getattr__したら存在しないのでエラーになったのだろう。

### ユーザ定義クラス

```python
class MyClass:
    def __init__(self, value=0): self.__value = value

s = MyClass()
print(s._MyClass__value)
s.__setattr__('_MyClass__value', 100)
print(s._MyClass__value)
```
```sh
$ python 1.py 
0
100
```

__setattr__は実装されているようだ。代入もできた。

### オーバーライドした

```python
class MyClass:
    def __init__(self, value=0): self.__value = value
    def __setattr__(self, name, value):
        print('__setattr__', name, value)
        super().__setattr__(name, value)
s = MyClass()
print(s._MyClass__value)
s.__setattr__('_MyClass__value', 100)
print(s._MyClass__value)
s._MyClass__value = 123
print(s._MyClass__value)
```
```sh
$ python 2.py 
__setattr__ _MyClass__value 0
0
__setattr__ _MyClass__value 100
100
__setattr__ _MyClass__value 123
123
```

