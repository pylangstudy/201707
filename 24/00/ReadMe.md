# [3.4.1. 待機可能オブジェクト (Awaitable Object)](https://docs.python.jp/3/reference/datamodel.html#awaitable-objects)

< [3.4. コルーチン](https://docs.python.jp/3/reference/datamodel.html#coroutines) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## 唐突

await、async、など初見キーワードが出てきた。この項はクラスの特性やカスタマイズなどについてだと思うが、そもそもawait, asyncについての説明や使い方を先にしてくれないと意味不明にも程がある。唐突すぎてついていけない。

一旦Python文書をかなぐり捨ててググる。

## 参考

* http://postd.cc/python-generators-coroutines-native-coroutines-and-async-await/
* http://d.hatena.ne.jp/minekoa/20070410/1176177653
* https://u7fa9.org/memo/HEAD/archives/2016-06/2016-06-25.rst

感謝。

### コルーチン

コルーチンとは、実行途中でreturnでき、次回呼出時に途中から再開できるもの。

Pythonでは以下の２種類の書き方があるっぽい。

* ジェネレータベースのコルーチン
* ネイティブコルーチン(await/async)

### ジェネレータベースのコルーチン

```python
import asyncio
import datetime
import random
 
@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
            yield from asyncio.sleep(random.randint(0, 5))

loop = asyncio.get_event_loop()
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
loop.run_forever()
```

* `@asyncio.coroutine`
* `yield from asyncio.sleep(...)`

### ネイティブコルーチン(await/async)

```python
import asyncio
import datetime
import random
 
async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))

loop = asyncio.get_event_loop() 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
loop.run_forever()
```

* `async def ...`
* `await asyncio.sleep(...)`

こちらのほうが記述が少なくて済む。

### 両者共通

どちらの方法でも以下のようなキーワードを使う。

* `import asyncio`
* `asyncio.get_event_loop()`
* `asyncio.ensure_future(...)`
* `loop.run_forever()`

### async関数内でyield関数を使用する

```python
import asyncio
import datetime
import random
import types

@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))

async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()

loop = asyncio.get_event_loop()
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
loop.run_forever()
```

* `@types.coroutine`

コルーチン内で別のコルーチンを使える。

