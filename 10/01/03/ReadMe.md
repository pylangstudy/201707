# [__repr__()](https://docs.python.jp/3/reference/datamodel.html#object.__repr__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> repr() 組み込み関数によって呼び出され、オブジェクトを表す「公式の (official)」文字列を計算します。可能なら、これは (適切な環境が与えられれば) 同じ値のオブジェクトを再生成するのに使える、有効な Python 式のようなものであるべきです。できないなら、 <...some useful description...> 形式の文字列が返されるべきです。戻り値は文字列オブジェクトでなければなりません。クラスが __repr__() を定義していて __str__() は定義していなければ、そのクラスのインスタンスの「非公式の (informal)」文字列表現が要求されたときにも __repr__() が使われます。

> この関数はデバッグの際によく用いられるので、たくさんの情報を含み、あいまいでないような表記にすることが重要です。

## 所感

* 用途がよくわからない
    * `オブジェクトを再生成するのに使える...文字列オブジェクト`の表現から察するに、シリアライズ・デシリアライズするのに使うのだろうか？
    * `デバッグの際によく用いられる`らしいので細かい情報も必要か

## ソースコード

```python
import datetime
print(int('100').__repr__())
print(str('abc').__repr__())
print(range(3).__repr__())
print(datetime.datetime.now().__repr__())
```
```sh
$ python3 0.py 
100
'abc'
range(0, 3)
datetime.datetime(2017, 7, 12, 9, 25, 54, 455603)
```

`range(0, 3)`はコンストラクタでこのインスタンスを生成できるPython式を表す文字列と思われる。datetimeも同様に、同一インスタンスを生成できるコンストラクタ式の文字列を返すようだ。

### ユーザ定義クラスでのデフォルト値

```python
class MyClass: pass
print(MyClass().__repr__())
```
```sh
$ python3 1.py 
<__main__.MyClass object at 0xb7156f0c>
```

フルネームや先頭アドレスと思われる16進数値が表示された。これでは再生性できないと思うのだが。前述の組込クラスに倣うなら、`__main__.MyClass()`か`MyClass()`が正しいのだろう。

### 状態なし

```python
class MyClass:
    def __repr__(self): return self.__class__.__name__ + '()'
print(MyClass().__repr__())
```

状態をひとつも持っていなければ簡単。

### 状態あり

```python
class MyClass:
    def __init__(self, value=0): self.__value = value
    def __repr__(self): return '{}({})'.format(self.__class__.__name__, self.__value)
print(MyClass(123).__repr__())
```
```sh
$ python3 3.py 
MyClass(123)
```

Python式にするなら注意点が多そう。

* コンストラクタ式だけで状態を完全に復元できるような実装でなくてはならない?
    * 複数の式でもOKだったり、`__attr`などを`_Classname__attr`として代入するなど強引に行っていいならその限りではないが
* 順序引数のときはその順序と値を紐付ける必要がある
* キーワード引数があるときはその名前と値を紐付ける必要がある


