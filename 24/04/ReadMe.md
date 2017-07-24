# [3.4.4. 非同期コンテクストマネージャ (Asynchronous Context Manager)](https://docs.python.jp/3/reference/datamodel.html#asynchronous-context-managers)

< [3.4. コルーチン](https://docs.python.jp/3/reference/datamodel.html#coroutines) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

コルーチンに関して理解できる情報がない。理解しようとするのを諦めた。

## Python文書

> 非同期コンテキストマネージャ は、 __aenter__ メソッドと __aexit__ メソッド内部で実行を一時停止できる コンテキストマネージャ です。

> 非同期コンテキストマネージャは async with 文の中で使えます。

### メソッド

メソッド|説明
--------|----
object.__aenter__(self)|このメソッドは文法的には __enter__() に似ていますが、 待機可能オブジェクト を返さなければならないところだけが異なります。
object.__aexit__(self, exc_type, exc_value, traceback)|このメソッドは文法的には __exit__() に似ていますが、 待機可能オブジェクト を返さなければならないところだけが異なります。

### 非同期コンテキストマネージャクラスの例

```python
class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context')

    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context')
```

> バージョン 3.5 で追加.

これをどうやって使えばいいのか。コード例がない。

