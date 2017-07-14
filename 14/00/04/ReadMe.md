# [__dir__(self)](https://docs.python.jp/3/reference/datamodel.html#object.__dir__)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> オブジェクトに dir() が呼び出されたときに呼び出されます。シーケンスが返されなければなりません。 dir() は返されたシーケンスをリストに変換し、ソートします。

## ソースコード

### オーバーライド

```python
class MyClass:
    def __init__(self, value=0): self.__value = value; self.name = 'name'
    def __dir__(self):
        print('__dir__')
        return super().__dir__()
s = MyClass()
print(dir(s))
```
```sh
 $ python 0.py 
__dir__
['_MyClass__value', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']
```

