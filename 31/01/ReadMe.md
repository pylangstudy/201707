# [4.5. イテレータ型](https://docs.python.jp/3/library/stdtypes.html#iterator-types)

< [4. 組み込み型](https://docs.python.jp/3/library/functions.html#built-in-functions) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [4.5. イテレータ型](https://docs.python.jp/3/library/stdtypes.html#iterator-types)

> Python はコンテナでの反復処理の概念をサポートしています。この概念は 2 つの別々のメソッドを使って実装されています; これらのメソッドを使ってユーザ定義のクラスで反復を行えるようにできます。後に詳しく述べるシーケンスは、必ず反復処理メソッドをサポートしています。

> コンテナオブジェクトに反復処理をサポートさせるためには、以下のメソッドを定義しなければなりません:

* container.__iter__()
* iterator.__iter__()
* iterator.__next__()

### 参考

Python文書では実装方法が不明。ググった。

* http://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09

## ソースコード

### Iterator実装

```python
class MyIterator(object):
    def __init__(self, *numbers):
        self._numbers = numbers
        self._i = 0
    def __iter__(self): return self
    def __next__(self):
        if self._i == len(self._numbers): raise StopIteration()
        value = self._numbers[self._i]
        self._i += 1
        return value


itr = MyIterator(10, 20, 30)
for num in itr: print('hello %d' % num)
```
```sh
$ python 0.py 
hello 10
hello 20
hello 30
```

### ループ数調整

3回ループする。

```python
class MyIterator(object):
    def __init__(self, *numbers):
        self._numbers = numbers
        self._i = 0
        self.__loop_count = 1
        self.__loop_limit = 3
    def __iter__(self): return self
    def __next__(self):
        if self._i == len(self._numbers):
            if self.__loop_limit <= self.__loop_count: raise StopIteration()
            else:
                self.__loop_count += 1
                self._i = 0
        value = self._numbers[self._i]
        self._i += 1
        return value


itr = MyIterator(10, 20, 30)
for num in itr: print('hello %d' % num)
```
```sh
$ python 1.py 
hello 10
hello 20
hello 30
hello 10
hello 20
hello 30
hello 10
hello 20
hello 30
```

色々カスタマイズできるのかもしれないが、用途が思いつかない。

