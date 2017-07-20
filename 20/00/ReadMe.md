# [3.3.3.5. クラスオブジェクトの作成](https://docs.python.jp/3/reference/datamodel.html#creating-the-class-object)

< [3.3.3. クラス生成をカスタマイズする](https://docs.python.jp/3/reference/datamodel.html#customizing-class-creation) < [3.3. 特殊メソッド名](https://docs.python.jp/3/reference/datamodel.html#special-method-names) < [3. データモデル](https://docs.python.jp/3/reference/datamodel.html#data-model) < [ドキュメント](https://docs.python.jp/3/index.html)

## Python文書の説明

> クラス本体の実行によってクラスの名前空間が初期化されたら、metaclass(name, bases, namespace, **kwds) を呼び出すことでクラスオブジェクトが作成されます (ここで渡される追加のキーワードは __prepare__ に渡されるものと同じです)。

> このクラスオブジェクトは、 super() の無引数形式によって参照されるものです。 __class__ は、クラス本体中のメソッドが __class__ または super のいずれかを参照している場合に、コンパイラによって作成される暗黙のクロージャー参照です。これは、メソッドに渡された最初の引数に基づいて現在の呼び出しを行うために使用されるクラスまたはインスタンスが識別される一方、 super() の無引数形式がレキシカルスコープに基づいて定義されているクラスを正確に識別することを可能にします。

意味不明。

### CPython 実装の詳細

> In CPython 3.6 and later, the __class__ cell is passed to the metaclass as a __classcell__ entry in the class namespace. If present, this must be propagated up to the type.__new__ call in order for the class to be initialised correctly. Failing to do so will result in a DeprecationWarning in Python 3.6, and a RuntimeWarning in the future.

>When using the default metaclass type, or any metaclass that ultimately calls type.__new__, the following additional customisation steps are invoked after creating the class object:

>    first, type.__new__ collects all of the descriptors in the class namespace that define a __set_name__() method;

>    second, all of these __set_name__ methods are called with the class being defined and the assigned name of that particular descriptor; and

>    finally, the __init_subclass__() hook is called on the immediate parent of the new class in its method resolution order.

[Google翻訳](https://translate.google.co.jp/?hl=ja#en/ja/In%20CPython%203.6%20and%20later%2C%20the%20__class__%20cell%20is%20passed%20to%20the%20metaclass%20as%20a%20__classcell__%20entry%20in%20the%20class%20namespace.%20If%20present%2C%20this%20must%20be%20propagated%20up%20to%20the%20type.__new__%20call%20in%20order%20for%20the%20class%20to%20be%20initialised%20correctly.%20Failing%20to%20do%20so%20will%20result%20in%20a%20DeprecationWarning%20in%20Python%203.6%2C%20and%20a%20RuntimeWarning%20in%20the%20future.%0A%0AWhen%20using%20the%20default%20metaclass%20type%2C%20or%20any%20metaclass%20that%20ultimately%20calls%20type.__new__%2C%20the%20following%20additional%20customisation%20steps%20are%20invoked%20after%20creating%20the%20class%20object%3A%0A%0A%20%20%20%20first%2C%20type.__new__%20collects%20all%20of%20the%20descriptors%20in%20the%20class%20namespace%20that%20define%20a%20__set_name__()%20method%3B%0A%20%20%20%20second%2C%20all%20of%20these%20__set_name__%20methods%20are%20called%20with%20the%20class%20being%20defined%20and%20the%20assigned%20name%20of%20that%20particular%20descriptor%3B%20and%0A%20%20%20%20finally%2C%20the%20__init_subclass__()%20hook%20is%20called%20on%20the%20immediate%20parent%20of%20the%20new%20class%20in%20its%20method%20resolution%20order.)

> CPython 3.6以降では、__class__セルがクラスネームスペースの__classcell__エントリとしてメタクラスに渡されます。 クラスが正しく初期化されるためには、これが型.__ new__を呼び出すまで伝播する必要があります。 そうしないと、Python 3.6でDeprecationWarningが発生し、将来はRuntimeWarningになります。

> デフォルトのメタクラス型または最終的にtype .__ new__を呼び出すメタクラスを使用する場合、クラスオブジェクトの作成後に次の追加のカスタマイズ手順が呼び出されます。

>     まず、.__ new__型は、__set_name __（）メソッドを定義するクラス名前空間内のすべての記述子を収集します。

>     第2に、これらの__set_name__メソッドはすべて、定義されているクラスとその特定の記述子の割り当てられた名前とともに呼び出されます。 そして

>     最後に、__init_subclass __（）フックが新しいクラスの直接の親に対してメソッド解決の順序で呼び出されます。


> クラスオブジェクトが作成された後には、クラス定義に含まれているクラスデコレータ (もしあれば) にクラスオブジェクトが渡され、デコレータが返すオブジェクトがここで定義されたクラスとしてローカルの名前空間に束縛されます。

> When a new class is created by type.__new__, the object provided as the namespace parameter is copied to a new ordered mapping and the original object is discarded. The new copy is wrapped in a read-only proxy, which becomes the __dict__ attribute of the class object.

[Google翻訳](https://translate.google.co.jp/?hl=ja#en/ja/When%20a%20new%20class%20is%20created%20by%20type.__new__%2C%20the%20object%20provided%20as%20the%20namespace%20parameter%20is%20copied%20to%20a%20new%20ordered%20mapping%20and%20the%20original%20object%20is%20discarded.%20The%20new%20copy%20is%20wrapped%20in%20a%20read-only%20proxy%2C%20which%20becomes%20the%20__dict__%20attribute%20of%20the%20class%20object.)

> .__ new__型で新しいクラスを作成すると、名前空間パラメータとして提供されたオブジェクトが新しい順序付けされたマッピングにコピーされ、元のオブジェクトは破棄されます。 新しいコピーは、クラスオブジェクトの__dict__属性となる読み取り専用プロキシにラップされます。

意味不明。

* デコレータの説明もしていないのにキーワードが出てきた
* `__classcell__`という属性があるらしい。

### 参考

* [PEP 3135](https://www.python.org/dev/peps/pep-3135) - New super

>    暗黙の __class__ クロージャ参照について記述しています

## 感想

意味不明。重要かどうかもわからない。読み流す。

