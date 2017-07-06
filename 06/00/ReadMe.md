# [2. 字句解析](https://docs.python.jp/3/reference/lexical_analysis.html#lexical-analysis)

< [ドキュメント](https://docs.python.jp/3/index.html)

## 字句解析

> Python で書かれたプログラムは パーザ (parser) に読み込まれます。パーザへの入力は、 字句解析器 (lexical analyzer) によって生成された一連の トークン (token) からなります。この章では、字句解析器がファイルをトークン列に分解する方法について解説します。

> Python はプログラムテキストを Unicode コードポイントとして読み込みます。ソースファイルのエンコーディングはエンコーディング宣言で与えられ、デフォルトは UTF-8 です。詳細は PEP 3120 を参照してください。ソースファイルがデコードできなければ、 SyntaxError が送出されます。

[PEP 3120](https://www.python.org/dev/peps/pep-3120)をみるとPython3のソースコードはUTF-8がデフォルトの文字コードと思われる。Python2は知らない。Windowsの場合も知らない。

## 構造

ソースコードの構造。

* [2.1. 行構造](https://docs.python.jp/3/reference/lexical_analysis.html#line-structure)
    * [2.1.1. 論理行](https://docs.python.jp/3/reference/lexical_analysis.html#logical-lines)
        * [2.1.5. 明示的な行継続](https://docs.python.jp/3/reference/lexical_analysis.html#explicit-line-joining)
        * [2.1.6. 非明示的な行継続](https://docs.python.jp/3/reference/lexical_analysis.html#implicit-line-joining)
    * [2.1.2. 物理行](https://docs.python.jp/3/reference/lexical_analysis.html#physical-lines)
    * [2.1.3. コメント](https://docs.python.jp/3/reference/lexical_analysis.html#comments)
    * [2.1.4. エンコード宣言](https://docs.python.jp/3/reference/lexical_analysis.html#encoding-declarations)
    * [2.1.7. 空行](https://docs.python.jp/3/reference/lexical_analysis.html#blank-lines)
    * [2.1.8. インデント](https://docs.python.jp/3/reference/lexical_analysis.html#indentation)
    * [2.1.9. トークン間の空白](https://docs.python.jp/3/reference/lexical_analysis.html#whitespace-between-tokens)
* [2.2. その他のトークン](https://docs.python.jp/3/reference/lexical_analysis.html#whitespace-between-tokens)
* [2.3. 識別子 (identifier) およびキーワード (keyword)](https://docs.python.jp/3/reference/lexical_analysis.html#identifiers)
    * [2.3.1. キーワード (keyword)](https://docs.python.jp/3/reference/lexical_analysis.html#keywords)
    * [2.3.2. 予約済みの識別子種 (reserved classes of identifiers)](https://docs.python.jp/3/reference/lexical_analysis.html#reserved-classes-of-identifiers)
* [2.4. リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#literals)
    * [2.4.1. 文字列およびバイト列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#string-and-bytes-literals)
    * [2.4.2. 文字列リテラルの結合 (concatenation)](https://docs.python.jp/3/reference/lexical_analysis.html#string-literal-concatenation)
    * [2.4.3. フォーマット済み文字列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#string-literal-concatenation)
    * [2.4.4. 数値リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#numeric-literals)
    * [2.4.5. 整数リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#integer-literals)
    * [2.4.6. 浮動小数点数リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#floating-point-literals)
    * [2.4.7. 虚数 (imaginary) リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#imaginary-literals)
* [2.5. 演算子](https://docs.python.jp/3/reference/lexical_analysis.html#operators)
* [2.6. デリミタ (delimiter)](https://docs.python.jp/3/reference/lexical_analysis.html#delimiters)

## [2.1. 行構造](https://docs.python.jp/3/reference/lexical_analysis.html#line-structure)

### [2.1.2. 物理行](https://docs.python.jp/3/reference/lexical_analysis.html#physical-lines)

* 物理行とは、行終端コードで区切られた文字列のこと
* 各プラットフォームごとの標準の行終端コードを使用する
    * これら全ての形式のコードは、違うプラットフォームでも等しく使用できる
        * Pythonに埋め込む場合には、標準のC言語の改行文字の変換規則`\n`を使う

OS|改行コード
--|----------
Unix|LF
Windows|CR+LF
Macintosh|CR

### [2.1.3. コメント](https://docs.python.jp/3/reference/lexical_analysis.html#comments)

* コメントは構文上無視される
* 文字列リテラル内に入っていないハッシュ文字 (#) から始まる
* 同じ物理行の末端で終わる
* 非明示的な行継続規則が適用されていない限り、コメントは論理行を終端させる

### [2.1.4. エンコード宣言](https://docs.python.jp/3/reference/lexical_analysis.html#encoding-declarations)

以下が推奨の記法らしい。
```python
# -*- coding: <encoding-name> -*-
```
```python
# vim:fileencoding=<encoding-name>
```

しかし冗長なため、しばしば以下のように書かれることもある。
```python
# encoding: utf-8
```
```python
# coding: utf-8
```

* 1行目または2行目に書いてあること
    * 2行目に書いてある場合、1行目もコメント行であること（大抵はshebang）
* `coding[=:]\s*([-\w.]+)`の正規表現にマッチすればいい。

### [2.1.7. 空行](https://docs.python.jp/3/reference/lexical_analysis.html#blank-lines)

* スペース、タブ、フォームフィード、およびコメントのみを含む論理行は無視される

### [2.1.8. インデント](https://docs.python.jp/3/reference/lexical_analysis.html#indentation)

Pythonにおける罠のひとつ。ハードタブは使わないほうが良い。使うとエラーになる場合がある。

* スペース
    * 最初の非空白文字までのスペースの総数が、その行のインデントを決定する
        * 言い換えると、Pythonは1行毎にインデントスペース数を変更できてしまう
* タブ
    * タブは1つにつき8つのスペースで置き換えられる
    * [TabError](http://docs.python.jp/3/library/exceptions.html#TabError)
        * タブとスペースを混在させ、その意味づけがタブのスペース換算数に依存するときはTabErrorになる

インデントも数が合わないとエラーになってしまう。以下のようなエラーがあるらしい。

```python
 def perm(l):                       # error: first line indented
for i in range(len(l)):             # error: not indented
    s = l[:i] + l[i+1:]
        p = perm(l[:i] + l[i+1:])   # error: unexpected indent
        for x in p:
                r.append(l[i:i+1] + x)
            return r                # error: inconsistent dedent
```

### [2.1.9. トークン間の空白](https://docs.python.jp/3/reference/lexical_analysis.html#whitespace-between-tokens)

スペースでトークンを分割する。

### [2.1.1. 論理行](https://docs.python.jp/3/reference/lexical_analysis.html#logical-lines)

#### [2.1.5. 明示的な行継続](https://docs.python.jp/3/reference/lexical_analysis.html#explicit-line-joining)

* `\`で複数行を1行として扱える
* バックスラッシュで終わる行にはコメントを入れることはできない

```python
if 0 == 0 \
    and 1 == 1 \
    and 2 == 2: # comment
        return 1
```

#### [2.1.6. 非明示的な行継続](https://docs.python.jp/3/reference/lexical_analysis.html#implicit-line-joining)

* 丸括弧 (parentheses)`()`、角括弧 (square bracket)`[]` 、および波括弧 (curly brace)`{}` 内の式は、バックスラッシュを使わずに一行以上の物理行に分割することができる
* 非明示的に継続された行にはコメントを含めることができる

```python
a = [1, # 1st
    2]  # 2nd
b = (3,
    4)
c = {'key1': 'val1',
    ''key2': 'val2'}
```

## [2.2. その他のトークン](https://docs.python.jp/3/reference/lexical_analysis.html#whitespace-between-tokens)

* NEWLINE、INDENT、DEDENT
* 識別子 (identifier), キーワード(keyword), リテラル, 演算子 (operator), デリミタ (delimiter) 

## [2.3. 識別子 (identifier) およびキーワード (keyword)](https://docs.python.jp/3/reference/lexical_analysis.html#identifiers)

* [PEP 3131](https://www.python.org/dev/peps/pep-3131)参照
* 識別子に使える文字は`[A-Za-z_0-9]`。ただし先頭文字に数字は使えない
    * Python3は上記のほかにUnicode文字が使える
        * https://www.dcl.hpi.uni-potsdam.de/home/loewis/table-3131.html

### [2.3.1. キーワード (keyword)](https://docs.python.jp/3/reference/lexical_analysis.html#keywords)

* 予約語である。識別子として使えない

```
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```

### [2.3.2. 予約済みの識別子種 (reserved classes of identifiers)](https://docs.python.jp/3/reference/lexical_analysis.html#reserved-classes-of-identifiers)

特殊な意味があるらしいので使わないほうが良いと思われる。

識別子|説明
------|----
`_*`|対話インタプリタで有効。直前に行われた評価の結果を記憶する
`__*__`|[特殊メソッド名](http://docs.python.jp/3/reference/datamodel.html#specialnames)などで話題に挙げられているらしい。用途不明。
`__*`|クラスプライベートな名前。[参照](http://docs.python.jp/3/reference/expressions.html#atom-identifiers)

意味不明だったが、もしや正規表現パターンか？`*`は0文字以上の文字を指しているのかもしれない。たとえば`_abc`, `__abc__`, `__abc`などを指しているのかもしれない。

## [2.4. リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#literals)

> リテラル (literal) とは、いくつかの組み込み型の定数を表記したものです。

### [2.4.1. 文字列およびバイト列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#string-and-bytes-literals)

> 文字列リテラルは以下の字句定義で記述されます:

```bnf
stringliteral   ::=  [stringprefix](shortstring | longstring)
stringprefix    ::=  "r" | "u" | "R" | "U" | "f" | "F"
                     | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
shortstring     ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
longstring      ::=  "'''" longstringitem* "'''" | '"""' longstringitem* '"""'
shortstringitem ::=  shortstringchar | stringescapeseq
longstringitem  ::=  longstringchar | stringescapeseq
shortstringchar ::=  <any source character except "\" or newline or the quote>
longstringchar  ::=  <any source character except "\">
stringescapeseq ::=  "\" <any source character>
```
```bnf
bytesliteral   ::=  bytesprefix(shortbytes | longbytes)
bytesprefix    ::=  "b" | "B" | "br" | "Br" | "bR" | "BR" | "rb" | "rB" | "Rb" | "RB"
shortbytes     ::=  "'" shortbytesitem* "'" | '"' shortbytesitem* '"'
longbytes      ::=  "'''" longbytesitem* "'''" | '"""' longbytesitem* '"""'
shortbytesitem ::=  shortbyteschar | bytesescapeseq
longbytesitem  ::=  longbyteschar | bytesescapeseq
shortbyteschar ::=  <any ASCII character except "\" or newline or the quote>
longbyteschar  ::=  <any ASCII character except "\">
bytesescapeseq ::=  "\" <any ASCII character>
```

前者は文字列、後者はバイト配列を表わした文字列のようだ。

* `'`または`"`で囲われる
    * 三重クォート`'''`または`"""`で囲うことも可能（ソースコード内の改行がそのまま反映される）
* `\`でメタ文字をエスケープする
* バイト列リテラルには、常に 'b' や 'B' が接頭する
    * [str](http://docs.python.jp/3/library/stdtypes.html#str) 型ではなく [bytes](http://docs.python.jp/3/library/functions.html#bytes) 型のインスタンスが作成される
* 接頭辞`u`(`U`)はユニコード文字であることを表す
    * Python3.3から再び可能になった。2.x以降かつ3.3以前の間では廃止されていた
        * [PEP414](https://www.python.org/dev/peps/pep-0414)
* 接頭辞`r`(`R`)はraw strings と呼ばれ、バックスラッシュをリテラル文字として扱う
* 接頭辞`f`(`F`)は[フォーマット済み文字列リテラル](http://docs.python.jp/3/reference/lexical_analysis.html#f-strings)である
* 各接頭辞には組合せられるものとできないものがある

エスケープ文字に関しては[Python文書](http://docs.python.jp/3/reference/lexical_analysis.html#string-and-bytes-literals)を参照。

### [2.4.2. 文字列リテラルの結合 (concatenation)](https://docs.python.jp/3/reference/lexical_analysis.html#string-literal-concatenation)

文字列同士は連結記号なしで連結できる。

> "hello" 'world'はhelloworld" と同じ

`()`内で論理行としてつなげつつ、1つの文字列として表現できる。`+`などの連結器号がなくとも良い。あってもよい。

```python
re.compile("[A-Za-z_]"       # letter or underscore
           "[A-Za-z0-9_]*"   # letter, digit or underscore
          )
```

> この機能は文法レベルで定義されていますが、スクリプトをコンパイルする際の処理として実現されることに注意してください。実行時に文字列表現を結合したければ、 ‘+’ 演算子を使わなければなりません。

どのような違いが生じるのか理解できない。


### [2.4.3. フォーマット済み文字列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#string-literal-concatenation)

Python3.6で追加された新機能らしい。

> 接頭辞 'f' または 'F' の付いた文字列リテラル

> 波括弧 {} で区切られた式である置換フィールドを含める

> 他の文字列リテラルの場合は内容が常に一定で変わることが無いのに対して、フォーマット済み文字列リテラルは実行時に式として評価されます。

```bnf
f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::=  "{" f_expression ["!" conversion] [":" format_spec] "}"
f_expression      ::=  (conditional_expression | "*" or_expr)
                         ("," conditional_expression | "," "*" or_expr)* [","]
                       | yield_expression
conversion        ::=  "s" | "r" | "a"
format_spec       ::=  (literal_char | NULL | replacement_field)*
literal_char      ::=  <any code point except "{", "}" or NULL>
```

ソースコードで見たほうが早い。Python3.6.1で動作確認した。

```python
name = 'Yamada'
a = f'My name is {name}.'
print(a)
```
```sh
$ python 0.py 
My name is Yamada.
```

これまでのPythonだと以下のようになる。

3.x
```python
name = 'Yamada'
a = 'My name is {name}.'.format(name=name)
print(a)
```
```python
name = 'Yamada'
a = 'My name is {0}.'.format(name)
print(a)
```
2.x
```python
name = 'Yamada'
a = 'My name is %s.' % name
print a
```

タイプ数と可読性のバランスがとれた記法に思える。ぜひとも使いたいが、Python3.6以降でないと使えないというのが厳しい。

細かいことは各文書を参照。

* http://docs.python.jp/3/reference/lexical_analysis.html#formatted-string-literals
* [PEP 498](https://www.python.org/dev/peps/pep-0498)
* [str.format](http://docs.python.jp/3/library/stdtypes.html#str.format)

### [2.4.4. 数値リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#numeric-literals)

* 整数 (integer) `0`, `-5`, `15`, `0xFF`, `0b1111`, `0o17`
* 浮動小数点数 (floating point number) `0.1`, `3.14`
* 虚数(imaginary numbers) `2j`, `1+4j`

### [2.4.5. 整数リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#integer-literals)

```bnf
integer      ::=  decinteger | bininteger | octinteger | hexinteger
decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
bininteger   ::=  "0" ("b" | "B") (["_"] bindigit)+
octinteger   ::=  "0" ("o" | "O") (["_"] octdigit)+
hexinteger   ::=  "0" ("x" | "X") (["_"] hexdigit)+
nonzerodigit ::=  "1"..."9"
digit        ::=  "0"..."9"
bindigit     ::=  "0" | "1"
octdigit     ::=  "0"..."7"
hexdigit     ::=  digit | "a"..."f" | "A"..."F"
```

整数リテラルの例

```
7     2147483647                        0o177    0b100110111
3     79228162514264337593543950336     0o377    0xdeadbeef
      100_000_000_000                   0b_1110_0101
```

> バージョン 3.6 で変更: グループ化を目的としたリテラル中のアンダースコアが許されるようになりました。

事前の説明が足りていない。以下で補足。

基数|接頭辞
----|-----
2|`0b`
8|`0o`
16|`0x`

たとえば10進数での`15`は各基数で以下のように表現できる。

基数|表記
----|----
10|`15`
16|`0xF`
2|`0b1111`
8|`0o17`

### [2.4.6. 浮動小数点数リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#floating-point-literals)

```bnf
floatnumber   ::=  pointfloat | exponentfloat
pointfloat    ::=  [digitpart] fraction | digitpart "."
exponentfloat ::=  (digitpart | pointfloat) exponent
digitpart     ::=  digit (["_"] digit)*
fraction      ::=  "." digitpart
exponent      ::=  ("e" | "E") ["+" | "-"] digitpart
```

浮動小数点数リテラルの例
```
3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93
```



### [2.4.7. 虚数 (imaginary) リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#imaginary-literals)

```bnf
imagnumber ::=  (floatnumber | digitpart) ("j" | "J")
```

虚数リテラルの例
```
3.14j   10.j    10j     .001j   1e100j   3.14e-10j   3.14_15_93j
```

## [2.5. 演算子](https://docs.python.jp/3/reference/lexical_analysis.html#operators)

```
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~
<       >       <=      >=      ==      !=
```

## [2.6. デリミタ (delimiter)](https://docs.python.jp/3/reference/lexical_analysis.html#delimiters)

字句を区切る文字。

```
(       )       [       ]       {       }
,       :       .       ;       @       =       ->
+=      -=      *=      /=      //=     %=      @=
&=      |=      ^=      >>=     <<=     **=
```

メタ文字
```
'       "       #       \
```

Pythonで使わない印字可能ASCII文字
```
$       ?       `
```

