# [3.2. 標準型の階層](https://docs.python.jp/3/reference/datamodel.html#the-standard-type-hierarchy)

< [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## 組込の型

> 以下は Python に組み込まれている型のリストです。(実装によって、C、Java、またはその他の言語で書かれた) 拡張モジュールで、その他の型が定義されていることがあります。新たな型 (有理数や、整数を効率的に記憶する配列、など) の追加は、たいてい標準ライブラリを通して提供されますが、将来のバージョンの Python では、型の階層構造にこのような追加がなされるかもしれません。

> 以下に説明する型のいくつかには、 ‘特殊属性 (special attribute)’ を列挙した段落があります。これらの属性は実装へのアクセス手段を提供するもので、一般的な用途に利用するためのものではありません。特殊属性の定義は将来変更される可能性があります。

* `None`
* [NotImplementedhttps](https://docs.python.jp/3/library/numbers.html#implementing-the-arithmetic-operations)
* `Ellipsis`
* [numbers.Number](https://docs.python.jp/3/library/numbers.html#numbers.Number)
    * [numbers.Integral](https://docs.python.jp/3/library/numbers.html#numbers.Integral)
        * [int](https://docs.python.jp/3/library/numbers.html#numbers.Integral)
        * [bool](https://docs.python.jp/3/library/functions.html#bool)
    * [numbers.Real](https://docs.python.jp/3/library/numbers.html#numbers.Real) ([float](https://docs.python.jp/3/library/functions.html#float))
    * [numbers.Complex](https://docs.python.jp/3/library/numbers.html#numbers.Complex) ([complex](https://docs.python.jp/3/library/functions.html#complex))
* シーケンス型
    * immutable
        * string
        * tuple
        * bytes
    * mutable
        * list
        * [bytearray](https://docs.python.jp/3/library/functions.html#bytearray)
        * [array](https://docs.python.jp/3/library/array.html#module-array)
        * [collections](https://docs.python.jp/3/library/collections.html#module-collections)モジュール参照
* 集合型
    * [set](https://docs.python.jp/3/library/stdtypes.html#set)
    * [frozenset](https://docs.python.jp/3/library/stdtypes.html#frozenset)
* マッピング型
    * dictionary
* [呼び出し可能型](https://docs.python.jp/3/reference/expressions.html#calls)
    * [ユーザ定義関数](https://docs.python.jp/3/reference/compound_stmts.html#function)
    * 特殊属性
        * `__doc__`
        * [__name__](https://docs.python.jp/3/library/stdtypes.html#definition.__name__)
        * [__qualname__](https://docs.python.jp/3/library/stdtypes.html#definition.__qualname__)
        * `__module__`
        * `__defaults__`
        * `__code__`
        * `__globals__`
        * [__dict__](https://docs.python.jp/3/library/stdtypes.html#object.__dict__)
        * `__closure__`
        * `__annotations__`
        * `__kwdefaults__`
    * インスタンスメソッド
    * [ジェネレータ関数](https://docs.python.jp/3/reference/simple_stmts.html#yield)
    * [コルーチン関数](https://docs.python.jp/3/reference/compound_stmts.html#async-def)
    * Asynchronous generator functions
    * 組み込み関数
    * 組み込みメソッド
    * クラス
    * クラスのインスタンス
* カスタムクラス型
* クラスインスタンス
* I/O オブジェクト
* 内部型
    * [bytecode](https://docs.python.jp/3/glossary.html#term-bytecode)
    * フレームオブジェクト
    * トレースバックオブジェクト
    * スライスオブジェクト
    * [静的メソッドオブジェクト](https://docs.python.jp/3/library/functions.html#staticmethod)
    * [クラスメソッドオブジェクト](https://docs.python.jp/3/library/functions.html#classmethod)

## 所感

以下、とくに意味不明だったもの。

* `__closure__`
* カスタムクラス型

クラス関係は全般的に意味不明だった。

すべてにおいて言えるが、動作するソースコードで示して欲しい。文章だけではさっぱりわからない。

* どうやって書くのか
* 何を意味するのか
    * 何をするための概念なのか
        * 使いどころはいつか

リンク先をみてみると、これから学習することになっている。わからないまま放置して進めることにする。
