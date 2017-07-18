# [3.3.3.2. 適切なメタクラスの決定](https://docs.python.jp/3/reference/datamodel.html#determining-the-appropriate-metaclass)

< [3.3.3. クラス生成をカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-class-creation) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> クラス定義に対して適切なメタクラスは、以下のように決定されます:

>    ベースクラスも明示的なメタクラスも指定されなかった場合、 type() が使われます

>    明示的にメタクラスが指定され、それが type() のインスタンス でない 場合、それが直接メタクラスとして使われます

>    type() のインスタンスが明示的にメタクラスとして指定されたり、ベースクラスが定義されている場合、最も派生的なメタクラスが使われます

>最も派生的なメタクラスは、(もしあれば) 明示的に指定されたメタクラスと、指定されたすべてのベースクラスのメタクラスから選ばれます。最も派生的なメタクラスは、これらのメタクラス候補のすべてのサブタイプであるようなものです。メタクラス候補のどれもその基準を満たさなければ、クラス定義は TypeError で失敗します。

ソースコードで提示してほしい。Python文書にはコード例が足りなさすぎる。

## ソースコード

### 継承なし

> クラス定義に対して適切なメタクラスは、以下のように決定されます:

>    ベースクラスも明示的なメタクラスも指定されなかった場合、 type() が使われます

つまり、`class MyClass(metaclass=SomeClass):`のように宣言せずとも、必ずメタクラスは存在するということか。

```python
class MyClass: pass
```

上記コードだと、メタクラスに`type()`が使われる、ということなのだろう。

### 継承

>    明示的にメタクラスが指定され、それが type() のインスタンス でない 場合、それが直接メタクラスとして使われます

おそらく、以下コードでは`Super`クラスのメタクラスとして`Base`が使われる、ということだろう。

```python
class Base: pass
class Super(metaclass=Base): pass
```

ただ、「type() のインスタンス でない 場合」なのかどうか不明。コード中で`type()`を使っていないが、すべてのクラス定義はtype()で代用できるらしい。Python内部でtype()を使っているかもしれない。

### 意味不明

> type() のインスタンスが明示的にメタクラスとして指定されたり、ベースクラスが定義されている場合、最も派生的なメタクラスが使われます

上記文章のすべてが意味不明。以下コードのようなことだろうか？

```python
b = type('Base', (object,), {})
class Super(metaclass=b): pass
```

実行するとエラーになった。違うらしい。どう書けばいいか不明。

```sh
$ python 2.py 
Traceback (most recent call last):
  File "2.py", line 2, in <module>
    class Super(metaclass=b): pass
TypeError: object() takes no parameters
```

以下の文言で表現されたものは、ソースコードでどう表現したものを指すのか？

* type() のインスタンス ?
* メタクラスとして指定される `class A(metaclass=B):`
* ベースクラスが定義される `class A(B):`
* 最も派生的なメタクラス ?

