# [3.4.3. 非同期イテレータ (Asynchronous Iterator)](https://docs.python.jp/3/reference/datamodel.html#asynchronous-iterators)

< [3.4. コルーチン](https://docs.python.jp/3/reference/datamodel.html#coroutines) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書

> 非同期イテラブル の __aiter__ の実装からは非同期のコードが呼べ、 非同期イテレータ の __anext__ メソッドからは非同期のコードが呼べます。

> 非同期イテレータは async for 文の中で使えます。

* [async for](https://docs.python.jp/3/reference/compound_stmts.html#async-for)

### メソッド

メソッド|説明
--------|----
object.__aiter__(self)|非同期イテレータ オブジェクトを返すべき。
object.__anext__(self)|イテレータの次の値を返す 待機可能オブジェクトを返すべき。反復処理が終了後に[StopAsyncIteration](https://docs.python.jp/3/library/exceptions.html#StopAsyncIteration)例外を送出すべき。

### [async for](https://docs.python.jp/3/reference/compound_stmts.html#async-for)

唐突に現れた構文。以下のようにして非同期イテレータをイテレーションする構文らしい。

```python
async for TARGET in ITER:
    BLOCK
else:
    BLOCK2
```

### 非同期イテラブルオブジェクトの例

```python
class Reader:
    async def readline(self): print('readline')
    def __aiter__(self): return self
    async def __anext__(self):
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val

async for a in Reader():
    print(a)
else:
    print('else')
```
```sh
$ python 0.py 
  File "0.py", line 10
    async for a in Reader():
            ^
SyntaxError: invalid syntax
```

エラーになった。動作できる完全なソースコード例がないから何が間違っているのか全くわからない。

### 注釈

> バージョン 3.5.2 で変更: CPython 3.5.2 以降では、 __aiter__ は 非同期イテレータ を直接返せます。 awaitable オブジェクトを返すと PendingDeprecationWarning が送出されます。

> CPython 3.5.x での後方互換性のあるコードを書くときに推奨される方法は、 __aiter__ から待機可能オブジェクトを返し続けることです。 PendingDeprecationWarning を避け、コードの後方互換性を保ちたい場合は、次のデコレータが使えます:

```python
import functools
import sys

if sys.version_info < (3, 5, 2):
    def aiter_compat(func):
        @functools.wraps(func)
        async def wrapper(self):
            return func(self)
        return wrapper
else:
    def aiter_compat(func):
        return func
```
```python
class AsyncIterator:

    @aiter_compat
    def __aiter__(self):
        return self

    async def __anext__(self):
        ...
```

> CPython 3.6 からは、 PendingDeprecationWarning は DeprecationWarning に置き換えられます。 CPython 3.7 では、 __aiter__ から待機可能オブジェクトを返すと RuntimeError が送出されます。

ようするに「言語仕様が二転三転し、バージョンごとに異なるからプログラマが各自バージョンごとに動作を工夫して実装しろ」ということか？もうPython使いたくなくなってきた。

コルーチンにおけるまともな説明はおろか、デコレータや`@functools.wraps`についても説明がない。何がどうなっているのか不明。動くコードがないから使い方も価値も不明。何一つ理解できない。

