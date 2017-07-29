# [3. 組み込み定数](https://docs.python.jp/3/library/functions.html#built-in-functions)

< [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

## [3. 組み込み定数](https://docs.python.jp/3/library/functions.html#built-in-functions)

```python
#!python3.6
#coding:utf-8
print(False)
print(True)
print(None)
print(NotImplemented)
print(Ellipsis) # ...と同じ
print(__debug__) # Python が -O オプションを有効にして開始されたのでなければ真
```
```sh
$ python 0.py 
False
True
None
NotImplemented
Ellipsis
True
```

## [3.1. site モジュールで追加される定数](https://docs.python.jp/3/library/constants.html#constants-added-by-the-site-module)

```python
$ python
Python 3.6.1 (default, Apr 24 2017, 22:16:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> copyright
Copyright (c) 2001-2017 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
>>> license
Type license() to see the full license text
>>> credits
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> quit()
$ 
```
```python
$ python
Python 3.6.1 (default, Apr 24 2017, 22:16:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
$ 
```

> 対話的インタープリタシェルで有用ですが、プログラム中では使うべきではありません。

