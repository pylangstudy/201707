# [3.4.2. コルーチンオブジェクト](https://docs.python.jp/3/reference/datamodel.html#coroutine-objects)

< [3.4. コルーチン](https://docs.python.jp/3/reference/datamodel.html#coroutines) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

何を言っているのか不明。メソッドの実装方法不明。コード書けそうにないので適当にスルーする。

## Python文書

> Coroutine オブジェクトは awaitable オブジェクトです。 __await__() を呼び出し、その返り値に対し反復処理をすることでコルーチンの実行を制御できます。 コルーチンの実行が完了し制御を戻したとき、イテレータは StopIteration を送出し、その例外の value 属性に返り値を持たせます。 コルーチンが例外を送出した場合は、イテレータにより伝搬されます。 コルーチンから StopIteration 例外を外に送出すべきではありません。

最初の一文から意味不明。

> コルーチンには以下に挙げるメソッドもあり、これらはジェネレータのメソッドからの類似です (ジェネレータ-イテレータメソッド を参照してください)。 ただし、ジェネレータと違って、コルーチンは反復処理を直接はサポートしていません。

* [ジェネレータ-イテレータメソッド](https://docs.python.jp/3/reference/expressions.html#generator-methods)

> バージョン 3.5.2 で変更: コルーチンで2回以上待機 (await) すると RuntimeError となります。

### メソッド

メソッド|説明
--------|----
coroutine.send(value)|コルーチンの実行を開始、再開する。
coroutine.throw(type[, value[, traceback]])|コルーチンで指定された例外を送出する。
coroutine.close()|コルーチンが自分自身の後片付けをし終了する。

