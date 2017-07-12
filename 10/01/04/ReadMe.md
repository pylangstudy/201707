# [__str__()](https://docs.python.jp/3/reference/datamodel.html#object.__str__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> オブジェクトの「非公式の (informal)」あるいは表示に適した文字列表現を計算するために、 str(object) と組み込み関数 format(), print() によって呼ばれます。戻り値は string オブジェクトでなければなりません。

> __str__() が有効な Python 表現を返すことが期待されないという点で、このメソッドは object.__repr__() とは異なります: より便利な、または簡潔な表現を使用することができます。

[__repr__()](https://docs.python.jp/3/reference/datamodel.html#object.__repr__)の類似関数らしい。人の目で見てわかりやすい情報を表示することが期待されているようだ。

```python
import datetime
print(int('100').__str__())
print(str('abc').__str__())
print(range(3).__str__())
print(datetime.datetime.now().__str__())
```
```sh
$ python3 0.py 
100
abc
range(0, 3)
2017-07-13 07:33:45.376071
```

```python
class Human:
    def __init__(self, name='name', age=0): self.__name = name; self.__age = age;
    def __repr__(self): return '{}(name={}, age={})'.format(self.__class__.__name__, self.__name, self.__age)
    def __str__(self): return '{} name:{} age:{}'.format(self.__class__.__name__, self.__name, self.__age)
c = Human(name='Yamada', age=100)
print(c.__repr__())
print(c.__str__())
```
```sh
$ python3 1.py 
Human(name=Yamada, age=100)
Human name:Yamada age:100
```

