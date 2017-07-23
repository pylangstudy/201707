# [3.4.1. 待機可能オブジェクト (Awaitable Object)](https://docs.python.jp/3/reference/datamodel.html#awaitable-objects)

< [3.4. コルーチン](https://docs.python.jp/3/reference/datamodel.html#coroutines) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

何を言っているのか不明。メソッドの実装方法不明。コード書けそうにないので適当にスルーする。

## Python文書

> awaitable オブジェクトは一般的には __await__() が実装されています。 async def 関数が返す Coroutine オブジェクトは待機可能です。

### 注釈

> types.coroutine() デコレータもしくは asyncio.coroutine() でデコレータが付けられたジェネレータから返される generator iterator オブジェクトも待機可能ですが、 __await__() は実装されていません。 

### メソッド

* object.__await__(self)

> iterator を返さなければなりません。 このメソッドは awaitable オブジェクトを実装するのに使われるべきです。 簡単のために、 asyncio.Future にはこのメソッドが実装され、 await 式と互換性を持つようになっています。

バージョン 3.5 で追加.

#### 参考

> 待機可能オブジェクトについてより詳しくは PEP 492 を参照してください。 

* [PEP 492](https://www.python.org/dev/peps/pep-0492)

