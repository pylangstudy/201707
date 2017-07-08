# [Python 言語リファレンス](https://docs.python.jp/3/reference/index.html)

< [ドキュメント](https://docs.python.jp/3/index.html)

## [1. はじめに](https://docs.python.jp/3/reference/introduction.html#introduction)

> このリファレンスマニュアルは、Python プログラミング言語自体に関する記述です。チュートリアルとして書かれたものではありません。

> 私は本マニュアルをできるだけ正確に書こうとする一方で、文法や字句解析以外の全てについて、形式化された仕様記述ではなく英語を使うことにしました。そうすることで、このドキュメントが平均的な読者にとってより読みやすくなっているはずですが、ややあいまいな部分も残っていることでしょう。従って、もし読者のあなたが火星から来ている人で、このドキュメントだけから Python を再度実装しようとしているのなら、色々と推測しなければならないことがあり、実際にはおそらく全く別の言語を実装する羽目になるでしょう。逆に、あなたが Python を利用しており、Python 言語のある特定の領域において、厳密な規則が何か疑問に思った場合、その答えはこのドキュメントで確実に見つけられることでしょう。もしより形式化された言語定義をお望みなら、あなたの時間を提供していただいてかまいません — もしくは、クローン生成装置でも発明してください :-)。

Pythonユーザとしては一読しておきたいところ。Python言語の前に英語を勉強すべきではないかと思わなくもないが。

> 実装に関する詳細を言語リファレンスのドキュメントに載せすぎるのは危険なことです — 実装は変更されるかもしれず、同じ言語でも異なる実装は異なった動作をするかもしれないからです。一方、CPython が広く使われている一つの Python 実装 (別の実装も支持され続けていますが) なので、特定のクセについては、特に実装によって何らかの制限が加えられている場合には、触れておく価値があります。従って、このテキスト全体にわたって短い “実装に関する注釈 (imprementation notes)” がちりばめられています。

注釈とやらはCPythonを基準としたもの、ということか。

> Python 実装はいずれも、数々の組み込みモジュールと標準モジュールが付属します。それらについては、 Python 標準ライブラリ でドキュメント化されています。いくつかの組み込みモジュールについては、言語定義と重要なかかわりをもっているときについて触れています。

ならば言語リファレンスを見れば大凡の枠組みは掴めそうか。元々それを期待しているのだが。

## [1.1. 別のPythonの実装](https://docs.python.jp/3/reference/introduction.html#alternate-implementations)

* CPython
* [Jython](http://www.jython.org/)
* [Python for .NET](http://www.jython.org/)
* [IronPython](http://ironpython.net/)
* [PyPy](http://pypy.org/)

CPythonが基本。C言語による実装。他にもJava, .NET Framework, Pythonで書かれたPython実装がある。

## [1.2. 本マニュアルにおける表記法](https://docs.python.jp/3/reference/introduction.html#notation)

### BNF 文法記法

> バッカス・ナウア記法（英: Backus-Naur form）とは、文脈自由文法を定義するのに用いられるメタ言語のこと

* https://ja.wikipedia.org/wiki/%E3%83%90%E3%83%83%E3%82%AB%E3%82%B9%E3%83%BB%E3%83%8A%E3%82%A6%E3%82%A2%E8%A8%98%E6%B3%95
* http://qiita.com/h_sakurai/items/3cc328a6db8941ac6336

「現在はこのBNFを拡張した[EBNF (Extended BNF)](https://ja.wikipedia.org/wiki/EBNF) が一般的に使われている」とこのことだが、Python文書ではBNF記法での記述らしい。

```sh
name      ::=  lc_letter (lc_letter | "_")*
lc_letter ::=  "a"..."z"
```

> 最初の行は、name が lc_letter の後ろにゼロ個またはそれ以上の lc_letter とアンダースコアが続いたものであることを示しています。そして、lc_letter は 'a' から 'z' までの何らかの文字一字であることを示します。 (この規則は、このドキュメントに記述されている字句規則と構文規則において定義されている名前 (name) で一貫して使われています)。

正規表現でいうと`[a-z_]*`だろうか？やたら冗長な記法に見えてしまう。

> 各規則は name (規則によって定義されているものの名前) と ::= から始まります。垂直線 (|) は、複数の選択項目を分かち書きするときに使います; この記号は、この記法において最も結合優先度の低い演算子です。アスタリスク (*) は、直前にくる要素のゼロ個以上の繰り返しを表します; 同様に、プラス (+) は一個以上の繰り返しで、角括弧 ([ ]) に囲われた字句は、字句がゼロ個か一個出現する (別の言い方をすれば、囲いの中の字句はオプションである) ことを示します。* および + 演算子の結合範囲は可能な限り狭くなっています; 字句のグループ化には丸括弧を使います。リテラル文字列はクオートで囲われます。空白はトークンを分割しているときのみ意味を持ちます。規則は通常、一行中に収められています; 多数の選択肢のある規則は、最初の行につづいて、垂直線の後ろに各々別の行として記述されます。

どうやら正規表現に近いメタ記号の使い方をするようだ。しかし、上記の例にないメタ記号の説明までされても混乱する。BNF記法とやらだけで混乱するのに。

> (上の例のような) 字句定義では、他に二つの慣習が使われています: 三つのドットで区切られている二つのリテラル文字は、二つの文字の ASCII 文字コードにおける (包含的な) 範囲から文字を一字選ぶことを示します。各カッコ中の字句 (<...>) は、定義済みのシンボルを記述する非形式的なやりかたです; 例えば、’制御文字’ を書き表す必要があるときなどに使われることがあります。

BNFの`...`は正規表現でいうところの`a-z`のときに使う`-`にあたると。

> 字句と構文規則の定義の間で使われている表記はほとんど同じですが、その意味には大きな違いがあります: 字句定義は入力ソース中の個々の文字を取り扱いますが、構文定義は字句解析で生成された一連のトークンを取り扱います。次節 (“字句解析”) における BNF はすべて字句定義のためのものです; それ以降の章では、構文定義のために使っています。

字句と構文規則の定義という2つの異なる概念があるらしい。そのへんから説明してくれると助かるのだが……。読み進めていけばわかるだろうか。

## 感想

率直な疑問なのだが、なぜPythonの言語仕様を知りたいのに、BNF記法とやらの勉強になっているのか？どうやらPython文書でPython言語仕様を知るには、事前に英語とBNF記法についての知識が必要らしい。ずいぶんと敷居の高いドキュメントに思える。

これを読む前は、チュートリアルで触れなかったデコレータなどの構文についてコードを交えて説明されるものとばかり思っていた。しかし蓋を開けてみれば、なぜか構文解析の話になっている。どうやらソースコードの文字列を解析するしくみを読者に投げつけるつもりらしい。期待していたのとずいぶん違うのだが……。Python言語の構文についての説明はあるのだろうか？詳細な字句解析など求めていない。不安。

チュートリアルの謎日本語とPythonへのネガティブ回避ヨイショ文法とはまた違う種類の解読スキルが必要になりそう。いずれにせよ言語リファレンスも難儀しそうな予感。
