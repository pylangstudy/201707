# [3.3.7. 数値型をエミュレーションする](https://docs.python.jp/3/reference/datamodel.html#emulating-numeric-types)

< [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 以下のメソッドを定義して、数値型オブジェクトをエミュレートすることができます。特定の種類の数値型ではサポートされていないような演算に対応するメソッド (非整数の数値に対するビット単位演算など) は、未定義のままにしておかなければなりません。

### 左辺被演算子メソッド

* object.__add__(self, other)
* object.__sub__(self, other)
* object.__mul__(self, other)
* object.__matmul__(self, other)
* object.__truediv__(self, other)
* object.__floordiv__(self, other)
* object.__mod__(self, other)
* object.__divmod__(self, other)
* object.__pow__(self, other[, modulo])
* object.__lshift__(self, other)
* object.__rshift__(self, other)
* object.__and__(self, other)
* object.__xor__(self, other)
* object.__or__(self, other)

> これらのメソッドを呼んで二項算術演算子 (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |) を実装します。 例えば x が __add__() メソッドのあるクラスのインスタンスである場合、式 x + y を評価すると x.__add__(y) が呼ばれます。 __divmod__() メソッドは __floordiv__() と __mod__() を使用するのと等価でなければなりません。 __truediv__() と関連してはなりません。 組み込みの pow() 関数の三項のものがサポートされていなければならない場合、 __pow__() はオプションの第三引数を受け取るものとして定義されなければなりません。

> これらのメソッドのいずれかが渡された引数に対する操作を提供していない場合、 NotImplemented を送出しなければなりません。

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __add__(self, other): return self.__value + other

c = MyClass(100)
print(c + 23)
print(23 + c)
```
```sh
$ python 0.py 
123
Traceback (most recent call last):
  File "0.py", line 7, in <module>
    print(23 + c)
TypeError: unsupported operand type(s) for +: 'int' and 'MyClass'
```

左辺なら加算できたが、右辺のときはできない。`__radd__`の実装が必要。

### 右辺被演算子メソッド

* object.__radd__(self, other)
* object.__rsub__(self, other)
* object.__rmul__(self, other)
* object.__rmatmul__(self, other)
* object.__rtruediv__(self, other)
* object.__rfloordiv__(self, other)
* object.__rmod__(self, other)
* object.__rdivmod__(self, other)
* object.__rpow__(self, other)
* object.__rlshift__(self, other)
* object.__rrshift__(self, other)
* object.__rand__(self, other)
* object.__rxor__(self, other)
* object.__ror__(self, other)

> These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation [3] and the operands are of different types. [4] For instance, to evaluate the expression x - y, where y is an instance of a class that has an __rsub__() method, y.__rsub__(x) is called if x.__sub__(y) returns NotImplemented.

[Google翻訳](https://translate.google.co.jp/?hl=ja#en/ja/These%20methods%20are%20called%20to%20implement%20the%20binary%20arithmetic%20operations%20(%2B%2C%20-%2C%20*%2C%20%40%2C%20%2F%2C%20%2F%2F%2C%20%25%2C%20divmod()%2C%20pow()%2C%20**%2C%20%3C%3C%2C%20%3E%3E%2C%20%26%2C%20%5E%2C%20%7C)%20with%20reflected%20(swapped)%20operands.%20These%20functions%20are%20only%20called%20if%20the%20left%20operand%20does%20not%20support%20the%20corresponding%20operation%20%5B3%5D%20and%20the%20operands%20are%20of%20different%20types.%20%5B4%5D%20For%20instance%2C%20to%20evaluate%20the%20expression%20x%20-%20y%2C%20where%20y%20is%20an%20instance%20of%20a%20class%20that%20has%20an%20__rsub__()%20method%2C%20y.__rsub__(x)%20is%20called%20if%20x.__sub__(y)%20returns%20NotImplemented.)

> これらのメソッドは、（+、 - 、*、@、/、//、％、divmod（）、pow（）、**、<<、>>、＆、^、|） 反映された（スワップされた）オペランド。 これらの関数は、左のオペランドが対応するオペレーション[3]をサポートせず、オペランドのタイプが異なる場合にのみ呼び出されます。 例えば、式x - yを評価するには、yが__rsub __（）メソッドを持つクラスのインスタンスで、x .__ sub __（y）がNotImplementedを返す場合はy __ rsub __（x）が呼び出されます。

> ただし、三項演算子 pow() が __rpow__() を呼ぶことはないので注意してください (型強制の規則が非常に難解になるからです)。

> 注釈

> 右側の被演算子の型が左側の被演算子の型のサブクラスであり、このサブクラスであるメソッドに対する反射メソッドが定義されている場合には、左側の被演算子の非反射メソッドが呼ばれる前に、このメソッドが呼ばれます。この振る舞いにより、サブクラスが親の演算をオーバーライドすることが可能になります。

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __radd__(self, other): return other + self.__value

c = MyClass(100)
print(23 + c)
print(c + 23)
```
```sh
$ python 1.py 
123
Traceback (most recent call last):
  File "1.py", line 7, in <module>
    print(c + 23)
TypeError: unsupported operand type(s) for +: 'MyClass' and 'int'
```

### 累算算術代入メソッド

* object.__iadd__(self, other)
* object.__isub__(self, other)
* object.__imul__(self, other)
* object.__imatmul__(self, other)
* object.__itruediv__(self, other)
* object.__ifloordiv__(self, other)
* object.__imod__(self, other)
* object.__ipow__(self, other[, modulo])
* object.__ilshift__(self, other)
* object.__irshift__(self, other)
* object.__iand__(self, other)
* object.__ixor__(self, other)
* object.__ior__(self, other)

> これらのメソッドを呼び出して累算算術代入 (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=) を実装します。 これらのメソッドは演算をインプレースで (self を変更する) 行うよう試み、その結果 (その必要はありませんが self でも構いません) を返さなければなりません。 特定のメソッドが定義されていない場合、その累算算術演算は通常のメソッドにフォールバックされます。 例えば x が __iadd__() メソッドを持つクラスのインスタンスである場合、x += y は x = x.__iadd__(y) と等価です。 そうでない場合、x + y の評価と同様に x.__add__(y) と y.__radd__(x) が考慮されます。 特定の状況では、累算代入は予期しないエラーに終わるかもしれません (なぜ加算はされるのに a_tuple[i] += [‘item’] は例外を送出するのですか? を参照してください) が、この挙動は実際はデータモデルの挙動の一部です。

[なぜ加算はされるのに a_tuple[i] += [‘item’] は例外を送出するのですか?](https://docs.python.jp/3/faq/programming.html#faq-augmented-assignment-tuple-error)

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __iadd__(self, other): self.__value += other; return self.__value;
c = MyClass(100)
c += 23
print(str(c))
```
```sh
$ python 2.py 
123
```

### 単項算術演算メソッド

* object.__neg__(self)
* object.__pos__(self)
* object.__abs__(self)
* object.__invert__(self)

> 呼び出して単項算術演算 (-, +, abs() および ~) を実装します。

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __neg__(self): return self.__value * -1;
c = MyClass(100)
print(str(-c))
```
```sh
$ python 3.py 
-100
```

### 丸めメソッド

* object.__complex__(self)
* object.__int__(self)
* object.__float__(self)
* object.__round__(self[, n])
* object.__index__(self)

> 呼び出して組み込み関数 complex() 、 int() 、 float() 、および round() を実装します。適切な型の値を返さなければなりません。

> 呼び出して operator.index() を実装します。 Python が数値オブジェクトを整数オブジェクトに損失なく変換する必要がある場合 (たとえばスライシングや、組み込みの bin() 、 hex() 、 oct() 関数) は常に呼び出されます。 このメソッドがあるとその数値オブジェクトが整数型であることが示唆されます。 整数を返さなければなりません。

> 注釈

> 整数型クラスの一貫性を保つため、__index__() が定義された場合、__int__() もまた定義されるべきであり、どちらも同じ値を返すべきです。

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __int__(self): return int(self.__value)
c = MyClass(1.23)
print(int(c))
```
```sh
$ python 4.py 
1
```
```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __int__(self): return int(self.__value)
    def __index__(self):
#        return index(self.__value) # NameError: name 'index' is not defined
        print('__index__')
        return int(self.__value)
c = MyClass(1)
print(int(c))
c = MyClass(1)
print(bin(c))
```
```sh
$ python 5.py 
1
__index__
0b1
```

