# [__delattr__(self, name)](https://docs.python.jp/3/reference/datamodel.html#object.__delattr__)

< [3.3.2. 属性値アクセスをカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-attribute-access) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> __setattr__() に似ていますが、代入ではなく値の削除を行います。このメソッドを実装するのは、オブジェクトにとって del obj.name が意味がある場合だけにしなければなりません。

たぶんファイルなどのリソース解放が必要な場合のみ実装しろということなのだろう。わざわざ__delattr__という特殊メソッドで実装する必要性が

## ソースコード

### オーバーライド

```python
class MyClass:
    def __init__(self, value=0): self.__value = value; self.name = 'name'
    def __delattr__(self, name):
        print('__delattr__')
        super().__delattr__(name)
s = MyClass()
print(s._MyClass__value)
print(s.name)
#s.__delattr__('_MyClass__value') # AttributeError: 'MyClass' object has no attribute '_MyClass__value'
#s.__delattr__('__value') # AttributeError: __value
s.__delattr__('name')
print(s._MyClass__value)
print(s.name)
```
```sh
$ python 0.py 
0
name
__delattr__
0
Traceback (most recent call last):
  File "0.py", line 13, in <module>
    print(s.name)
AttributeError: 'MyClass' object has no attribute 'name'
```

