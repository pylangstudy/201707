# [3.3.8. with文とコンテキストマネージャ](https://docs.python.jp/3/reference/datamodel.html#with-statement-context-managers)

< [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## [with](https://docs.python.jp/3/reference/compound_stmts.html#with)

> コンテキストマネージャ(context manager) とは、 with 文の実行時にランタイムコンテキストを定義するオブジェクトです。コンテキストマネージャは、コードブロックを実行するために必要な入り口および出口の処理を扱います。コンテキストマネージャは通常、 with 文（ with 文 の章を参照）により起動されますが、これらのメソッドを直接呼び出すことで起動することもできます。

> コンテキストマネージャの代表的な使い方としては、様々なグローバル情報の保存および更新、リソースのロックとアンロック、ファイルのオープンとクローズなどが挙げられます。

> コンテキストマネージャについてのさらなる情報については、 コンテキストマネージャ型 を参照してください。

[コンテキストマネージャ型](https://docs.python.jp/3/library/stdtypes.html#typecontextmanager)



### object.__enter__(self)

> コンテキストマネージャのの入り口で実行される処理です。 with 文は、文の as 節で規定された値を返すこのメソッドを呼び出します。

### object.__exit__(self, exc_type, exc_value, traceback)

> コンテキストマネージャの出口で実行される処理です。パラメータは、コンテキストが終了した原因となった例外について説明しています。コンテキストが例外を送出せず終了した場合は、全ての引き数に None が設定されます。

> もし、例外が送出され、かつメソッドが例外を抑制したい場合（すなわち、例外が伝播されるのを防ぎたい場合）、このメソッドは True を返す必要があります。そうでなければ、このメソッドの終了後、例外は通常通り伝播することになります。

> __exit__() メソッドは受け取った例外を再度送出すべきではありません。これは、呼び出し側の責任でおこなってください。


## ソースコード

### 実行確認

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __enter__(self):
        print('__enter__')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', exc_type, exc_value, traceback)

with MyClass(100) as c:
    print('in with')
```
```sh
$ python 0.py 
__enter__
in with
__exit__ None None None
```

### 異常時の引数確認

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __enter__(self): print('__enter__')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', exc_type, exc_value, traceback)

with MyClass(100) as c:
    print('in with')
    raise Exception()
```
```sh
$ python 1.py 
__enter__
in with
__exit__ <class 'Exception'>  <traceback object at 0xb70e93c4>
Traceback (most recent call last):
  File "1.py", line 9, in <module>
    raise Exception()
Exception
```

### 異常時はTrueを返すべき

```python
class MyClass:
    def __init__(self, value): self.__value = value
    def __enter__(self): print('__enter__')
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__', exc_type, exc_value, traceback)
        if exc_type: return True

with MyClass(100) as c:
    print('in with')
    raise Exception()
```
```sh
$ python 2.py 
__enter__
in with
__exit__ <class 'Exception'>  <traceback object at 0xb715c39c>
```

> 例外が伝播されるのを防ぎたい場合...True を返す必要があります。

> __exit__() メソッドは受け取った例外を再度送出すべきではありません。


ということなので、例外があるときは`return True`する。

