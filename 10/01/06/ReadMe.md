# [__format__()](https://docs.python.jp/3/reference/datamodel.html#object.__format__)

< [3.3.1. 基本的なカスタマイズ](https://docs.python.jp/3/reference/datamodel.html#basic-customization) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> Called by the format() built-in function, and by extension, evaluation of formatted string literals and the str.format() method, to produce a “formatted” string representation of an object. The format_spec argument is a string that contains a description of the formatting options desired. The interpretation of the format_spec argument is up to the type implementing __format__(), however most classes will either delegate formatting to one of the built-in types, or use a similar formatting option syntax.

> 標準のフォーマット構文の解説は、 書式指定ミニ言語仕様 を参照してください。

> 戻り値は文字列オブジェクトでなければなりません。

> バージョン 3.4 で変更: 空でない文字列が渡された場合 object 自身の __format__ メソッドは TypeError を送出します。

和訳されていない……。[書式指定ミニ言語仕様](https://docs.python.jp/3/library/string.html#formatspec)参照。

## ソースコード

```python
import datetime
print(int('100').__format__('+'))
print(int('-100').__format__('+'))
print(str('abc').__format__('>5'))
#print(range(3).__format__('='))
print(datetime.datetime.now().__format__('%Y-%m-%d %H:%M:%S'))
```
```sh
$ python3 0.py 
+100
-100
  abc
2017-07-13 07:57:57
```

### 実装してみた

```python 
class Human:
    def __init__(self, name='name', age=0):
        self.__name = name
        self.__age = age
    def __format__(self, format_spec):
        if 'name' == format_spec: return self.__name
        elif 'age' == format_spec: return str(self.__age)
        else: return self.__str__()

h = Human()
print('{:name}'.format(h))
print('{:age}'.format(h))
```
```sh
$ python3 1.py 
name
0
```

http://postd.cc/new-string-formatting-in-python/

