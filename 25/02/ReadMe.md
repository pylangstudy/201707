# [2. 組み込み関数](https://docs.python.jp/3/library/functions.html#built-in-functions)

< [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## 一覧

* 68関数

```python
abs()
dict()
help()
min()
setattr()
all()
dir()
hex()
next()
slice()
any()
divmod()
id()
object()
sorted()
ascii()
enumerate()
input()
oct()
staticmethod()
bin()
eval()
int()
open()
str()
bool()
exec()
isinstance()
ord()
sum()
bytearray()
filter()
issubclass()
pow()
super()
bytes()
float()
iter()
print()
tuple()
callable()
format()
len()
property()
type()
chr()
frozenset()
list()
range()
vars()
classmethod()
getattr()
locals()
repr()
zip()
compile()
globals()
map()
reversed()
__import__()
complex()
hasattr()
max()
round()
delattr()
hash()
memoryview()
set()
```

以下のようなものがあった。

* 組み込み関数
* 組み込みクラス
* デコレータ（糖衣構文）
    * staticmethod
    * classmethod
    * property
    * setter
    * deleter
* コレクション操作系関数
* 別パッケージ利用の推奨

### classmethod

意外なことに、Python言語仕様と思っていた`@classmethod`について、ライブラリの章に書いてあった。

デコレータについてPython文書では意味不明のためググった。感謝。

* http://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e
* http://www17.atpages.jp/~lambda7/py/decorator.html




