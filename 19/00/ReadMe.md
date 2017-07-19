# [3.3.3.4. クラス本体の実行](https://docs.python.jp/3/reference/datamodel.html#executing-the-class-body)

< [3.3.3. クラス生成をカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-class-creation) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> クラス本体が (大まかには) exec(body, globals(), namespace) として実行されます。通常の呼び出しと exec() の重要な違いは、クラス定義が関数内部で行われる場合、レキシカルスコープによってクラス本体 (任意のメソッドを含む) が現在のスコープと外側のスコープから名前を参照できるという点です。

* [exec()](https://docs.python.jp/3/library/functions.html#exec)

> However, even when the class definition occurs inside the function, methods defined inside the class still cannot see names defined at the class scope. Class variables must be accessed through the first parameter of instance or class methods, or through the implicit lexically scoped __class__ reference described in the next section.

> ただし、関数内でクラス定義が発生しても、クラス内で定義されたメソッドは、クラススコープで定義された名前を参照できません。 クラス変数は、次のセクションで説明する暗黙のレキシカルスコープの__class__参照を介して、インスタンスまたはクラスのメソッドの最初のパラメータを通じてアクセスする必要があります。

* [Google翻訳](https://translate.google.co.jp/?hl=ja#en/ja/However%2C%20even%20when%20the%20class%20definition%20occurs%20inside%20the%20function%2C%20methods%20defined%20inside%20the%20class%20still%20cannot%20see%20names%20defined%20at%20the%20class%20scope.%20Class%20variables%20must%20be%20accessed%20through%20the%20first%20parameter%20of%20instance%20or%20class%20methods%2C%20or%20through%20the%20implicit%20lexically%20scoped%20__class__%20reference%20described%20in%20the%20next%20section.)

## 感想

何を言っているのかわからない。読み流そう。

### レキシカルスコープって何？

http://qiita.com/geshi/items/5cdcbdf615f69bbc09d4

ソースコード解析にて、定義前の名前は参照できない。

### 関数内部でクラス定義できるのか？

```python
def f():
    class MyClass: pass
    c = MyClass()
    print(dir(c))

#c = MyClass() # NameError: name 'MyClass' is not defined
#c = f.MyClass() # AttributeError: 'function' object has no attribute 'MyClass'
f()
```
```sh
$ python 0.py 
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

できた。しかし、関数の外側から参照することはできないようだ。おそらく変数と同様、関数内でのローカル変数として扱われるのだろう。

### exec(body, globals(), namespace)？

* [exec()](https://docs.python.jp/3/library/functions.html#exec)はPythonのコードを動的実行する組込関数である
* bodyとは何か？
* [globals()](https://docs.python.jp/3/library/functions.html#globals)とはグローバル変数の辞書である
* namespaceとは何か？

「クラス本体の通常の呼出とexec()の重要な違いは…」のように比較していることから、exec()でもクラス定義ができるのだろう。ただし、exec()の外側(呼出元)ではそのクラスは参照できない、と言っているのだろう。

### exec()でクラス生成してみる。

```python
code = '''
class MyClass: pass
c = MyClass()
print(c.__class__.__name__)
'''
ret = exec(code, globals(), locals())
print(ret)
c = MyClass()
print(c.__class__.__name__)
```
```sh
$ python 1.py 
MyClass
None
MyClass
```

できた。

### exec()の関数内でclass定義

```python
code = '''
def f():
    class MyClass: pass
    c = MyClass()
    print(c.__class__.__name__)
'''
ret = exec(code, globals(), locals())
print(ret)
#c = MyClass() # NameError: name 'MyClass' is not defined
#c = f.MyClass() # AttributeError: 'function' object has no attribute 'MyClass'
#print(c.__class__.__name__)
f()
```
```sh
$ python 2.py 
None
MyClass
```

ただ、ふつうにクラス定義したのと、exec()に違いが無いように見える。「現在のスコープと外側のスコープから名前を参照できる」という点が違うらしいが。

どちらの場合でも、関数内で定義した場合、関数外から参照できない。

何か勘違いしているかも知れないが、わからない。

### exec()コード内で関数内クラスを関数外から参照しようとしてみる

参照できなかった。「現在のスコープと外側のスコープから名前を参照できる」の意味が違うのか？

```python
code = '''
def f():
    class MyClass: pass
    c = MyClass()
    print(c.__class__.__name__)
#c = MyClass() # NameError: name 'MyClass' is not defined
#print(c.__class__.__name__)
'''
ret = exec(code, globals(), locals())
print(ret)
f()
```
```sh
$ python 3.py 
Traceback (most recent call last):
  File "3.py", line 9, in <module>
    ret = exec(code, globals(), locals())
  File "<string>", line 6, in <module>
NameError: name 'MyClass' is not defined
```

