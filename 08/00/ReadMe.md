# [3.2. 標準型の階層](https://docs.python.jp/3/reference/datamodel.html#the-standard-type-hierarchy)

< [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## 組込の型

> 以下は Python に組み込まれている型のリストです。(実装によって、C、Java、またはその他の言語で書かれた) 拡張モジュールで、その他の型が定義されていることがあります。新たな型 (有理数や、整数を効率的に記憶する配列、など) の追加は、たいてい標準ライブラリを通して提供されますが、将来のバージョンの Python では、型の階層構造にこのような追加がなされるかもしれません。

> 以下に説明する型のいくつかには、 ‘特殊属性 (special attribute)’ を列挙した段落があります。これらの属性は実装へのアクセス手段を提供するもので、一般的な用途に利用するためのものではありません。特殊属性の定義は将来変更される可能性があります。

型|説明
--|----
`None`|値が存在しないことを示す。
`NotImplemented`|未実装を示す。数値演算や拡張比較メソッドの実装がない場合に返すべき値。[参考](https://docs.python.jp/3/library/numbers.html#implementing-the-arithmetic-operations)
`Ellipsis`|リテラル`...`または組み込み名`Ellipsis`でアクセスされる
[numbers.Number](https://docs.python.jp/3/library/numbers.html#numbers.Number)|数値リテラル、算術演算、算術関数によって返されるオブジェクト。
  [numbers.Integral](https://docs.python.jp/3/library/numbers.html#numbers.Integral)|整数を表す
    [int](https://docs.python.jp/3/library/numbers.html#numbers.Integral)|整数。メモリが許す範囲で無限。
    [bool](https://docs.python.jp/3/library/functions.html#bool)|整数。`False`と`True`の2値を表す。0と1のように振る舞う。
  [numbers.Real](https://docs.python.jp/3/library/numbers.html#numbers.Real) ([float](https://docs.python.jp/3/library/functions.html#float))|倍精度浮動小数点数を表す。Pythonは単精度浮動小数点数をサポートしない。
  [numbers.Complex](https://docs.python.jp/3/library/numbers.html#numbers.Complex) ([complex](https://docs.python.jp/3/library/functions.html#complex))|倍精度浮動小数点を2つ一組にして複素数を表す。
シーケンス型|
  immutable|
    string|U+0000 - U+10FFFF。[ord()](https://docs.python.jp/3/library/functions.html#ord)と[chr()](https://docs.python.jp/3/library/functions.html#chr)で文字コード整数値と文字とを相互変換する。[str.encode()](https://docs.python.jp/3/library/stdtypes.html#str.encode)と[bytes.decode()](https://docs.python.jp/3/library/stdtypes.html#bytes.decode)とでバイナリ配列と文字列を相互変換する。
    tuple|`t = (1, 2)`のように表す。
    bytes|0 <= x < 256 の範囲の整数で表す。`b'abc'`のようなリテラル表現もできる。[bytes()](https://docs.python.jp/3/library/functions.html#bytes)でオブジェクト生成できる。
  mutable|
    list|`l = [1,2]`のように表す。
    [bytearray](https://docs.python.jp/3/library/functions.html#bytearray)|
    他|[array](https://docs.python.jp/3/library/array.html#module-array), [collections](https://docs.python.jp/3/library/collections.html#module-collections)モジュール参照
集合型|順序のない、ユニークで不変なオブジェクトの集合。
  [set](https://docs.python.jp/3/library/stdtypes.html#set)|
  [frozenset](https://docs.python.jp/3/library/stdtypes.html#frozenset)|[ハッシュ可能](https://docs.python.jp/3/glossary.html#term-hashable) (別の集合型の要素や辞書のキーにできる)
マッピング型|
  dictionary|`dict`型。`d = {'key': 'value'}`のように表す。`d['key']`のように参照する。[dbm.ndbm](https://docs.python.jp/3/library/dbm.html#module-dbm.ndbm), [dbm.gnu](https://docs.python.jp/3/library/dbm.html#module-dbm.gnu)
呼び出し可能型|[関数呼び出し操作](https://docs.python.jp/3/reference/expressions.html#calls)を行える型。
  [ユーザ定義関数](https://docs.python.jp/3/reference/compound_stmts.html#function)|[関数定義](https://docs.python.jp/3/reference/compound_stmts.html#function)を行うことで生成される。
  特殊属性|
    `__doc__`|ドキュメンテーション文字列
    [__name__](https://docs.python.jp/3/library/stdtypes.html#definition.__name__)|関数名
    [__qualname__](https://docs.python.jp/3/library/stdtypes.html#definition.__qualname__)|修飾名。関数の[qualified-name](https://docs.python.jp/3/glossary.html#term-qualified-name)。バージョン3.3で追加。
    `__module__`|モジュール名
    `__defaults__`|デフォルト値をもつ引数のデフォルト値が入ったタプル。
    `__code__`|コンパイルされた関数本体
    `__globals__`|グローバル変数のdict
    [__dict__](https://docs.python.jp/3/library/stdtypes.html#object.__dict__)|任意の関数属性をサポートするための名前空間
    `__closure__`|None または関数の個々の自由変数 (引数以外の変数) に対して値を結び付けているセル (cell) 群からなるタプル
    `__annotations__`|パラメータの注釈が入った辞書
    `__kwdefaults__`|キーワード専用パラメータのデフォルト値を含む辞書
  インスタンスメソッド|`def f(self):`のように定義する。
  ジェネレータ関数|[yield](https://docs.python.jp/3/reference/simple_stmts.html#yield)文を使った関数。
  コルーチン関数|[async def](https://docs.python.jp/3/reference/compound_stmts.html#async-def)で定義された関数。
  Asynchronous generator functions|和訳されていない…
  組み込み関数|C関数へのラッパー。[len()](https://docs.python.jp/3/library/functions.html#len)など。
  組み込みメソッド|実際には組み込み関数を別の形で隠蔽したもの。
  クラス|[__new__](https://docs.python.jp/3/reference/datamodel.html#object.__new__), [__init__](https://docs.python.jp/3/reference/datamodel.html#object.__init__)で呼び出し時の処理を定義できる。
  クラスのインスタンス|[__call__()](https://docs.python.jp/3/reference/datamodel.html#object.__call__)メソッドを定義することで呼び出し可能
モジュール|pythonソースコードのファイル単位。[import](https://docs.python.jp/3/reference/simple_stmts.html#import)文や[importlib.import_module](https://docs.python.jp/3/library/importlib.html#importlib.import_module)で取り込むことで起動する[importsystem](https://docs.python.jp/3/reference/import.html#importsystem)により生成される。
カスタムクラス型|
クラスインスタンス|
I/O オブジェクト|[file-object](https://docs.python.jp/3/glossary.html#term-file-object)
内部型|インタプリタが内部的に使っている型。変更される可能性がある。
  コードオブジェクト|[bytecode](https://docs.python.jp/3/glossary.html#term-bytecode)。
  フレームオブジェクト|実行フレーム。トレースバックオブジェクト内に出現する。
  トレースバックオブジェクト|例外のスタックトレースを表す。`sys.exc_info()`が返すタプルの三番目の要素。
  スライスオブジェクト|[__getitem__](https://docs.python.jp/3/reference/datamodel.html#object.__getitem__)メソッドのためのスライスを表すのに使われる。[slice()](https://docs.python.jp/3/library/functions.html#slice)でも生成できる。
  静的メソッドオブジェクト|関数オブジェクトからメソッドオブジェクトへの変換を阻止するための方法を提供する。[staticmethod()](https://docs.python.jp/3/library/functions.html#staticmethod)で生成する。
  クラスメソッドオブジェクト|別のオブジェクトを包むラッパであり、そのオブジェクトをクラスやクラスインスタンスから取り出す方法を代替する。[classmethod()](https://docs.python.jp/3/library/functions.html#classmethod)で生成する。

以下、とくに意味不明だったもの。

* __closure__
* カスタムクラス型

クラス関係は全般的に意味不明だった。

すべてにおいて言えるが、動作するソースコードで示して欲しい。文章だけではさっぱりわからない。

* どうやって書くのか
* 何を意味するのか
    * 何をするための概念なのか
        * 使いどころはいつか

リンク先をみてみると、これから学習することになっている。わからないまま放置して進める。
