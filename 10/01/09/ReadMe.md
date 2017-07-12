# [__bool__()](https://docs.python.jp/3/reference/datamodel.html#object.__bool__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> 真理値テストや組み込み演算 bool() を実装するために呼び出されます; False または True を返さなければなりません。このメソッドが定義されていないとき、 __len__() が定義されていれば呼び出され、その結果が非 0 であれば真とみなされます。クラスが __len__() も __bool__() も定義していないければ、そのクラスのインスタンスはすべて真とみなされます。

## ソースコード

```python
class Switch:
    def __init__(self, switch=False):
        self.__switch = switch
    def switch(self): self.__switch = not(self.__switch)
    def __bool__(self): return self.__switch

s = Switch()
print(s.__bool__())
s.switch()
print(s.__bool__())
```
```sh
$ python3 0.py 
False
True
```

