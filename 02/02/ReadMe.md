# [14. 対話入力編集と履歴置換](https://docs.python.jp/3/tutorial/whatnow.html#what-now)

< [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

今回は複数の項目を1つのReadMeで済ませる。

## [GNU Readline](https://tiswww.case.edu/php/chet/readline/rltop.html)ライブラリ

> いくつかのバージョンの Python インタプリタでは、Korn シェルや GNU Bash シェルに見られる機能に似た、現在の入力行に対する編集機能や履歴置換機能をサポートしています。この機能は様々な編集スタイルをサポートしている、GNU Readline ライブラリを使って実装されています。このライブラリには独自のドキュメントがあり、ここでそれを繰り返すつもりはありません。

## [14.1. タブ補完と履歴編集](https://docs.python.jp/3/tutorial/interactive.html#tab-completion-and-history-editing)

> 変数とモジュール名の補完はインタプリタの起動時に 自動的に有効化されます 。 従って Tab キーは補完機能を呼び出し、Python の文の名前、現在のローカル変数、および利用可能なモジュール名を検索します。string.a のようなドットで区切られた式については、最後の '.' までの式を評価し、結果として得られたオブジェクトの属性から補完候補を示します。 __getattr__() メソッドを持ったオブジェクトが式に含まれている場合、 __getattr__() がアプリケーション定義のコードを実行するかもしれないので注意してください。デフォルトの設定ではあなたのユーザーディレクトリの .python_history という名前のファイルに履歴を保存します。 履歴は次の対話的なインタプリタのセッションで再び利用することができます。

## [14.2. 対話的インタープリタの代替](https://docs.python.jp/3/tutorial/interactive.html#alternatives-to-the-interactive-interpreter)

> この機能は、初期の版のインタープリタに比べれば大きな進歩です。とはいえ、まだいくつかの要望が残されています。例えば、行を継続するときに正しいインデントが提示されたら快適でしょう (パーサは次の行でインデントトークンが必要かどうかを知っています)。補完機構がインタープリタのシンボルテーブルを使ってもよいかもしれません。括弧やクォートなどの対応をチェックする (あるいは指示する) コマンドも有用でしょう。

### [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html) IPython

> より優れた対話的インタープリタの代替の一つに IPython があります。このインタープリタは、様々なところで使われていて、タブ補完、オブジェクト探索や先進的な履歴管理といった機能を持っています。他のアプリケーションにカスタマイズされたり、組込まれこともあります。別の優れたインタラクティブ環境としては bpython があります。

#### インストール

http://pythondatascience.plavox.info/python%E3%81%AE%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83/jupyter-notebook%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86

```sh
$ pip3 install jupyter
Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl
Collecting qtconsole (from jupyter)
  Downloading qtconsole-4.3.0-py2.py3-none-any.whl (108kB)
    100% |████████████████████████████████| 112kB 903kB/s 
Collecting jupyter-console (from jupyter)
  Downloading jupyter_console-5.1.0-py2.py3-none-any.whl
Collecting nbconvert (from jupyter)
  Downloading nbconvert-5.2.1-py2.py3-none-any.whl (382kB)
    100% |████████████████████████████████| 389kB 741kB/s 
Collecting ipywidgets (from jupyter)
  Downloading ipywidgets-6.0.0-py2.py3-none-any.whl (46kB)
    100% |████████████████████████████████| 51kB 2.8MB/s 
Collecting ipykernel (from jupyter)
  Downloading ipykernel-4.6.1-py3-none-any.whl (104kB)
    100% |████████████████████████████████| 112kB 1.6MB/s 
Collecting notebook (from jupyter)
  Downloading notebook-5.0.0-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 6.9MB 45kB/s 
Collecting pygments (from qtconsole->jupyter)
  Using cached Pygments-2.2.0-py2.py3-none-any.whl
Collecting ipython-genutils (from qtconsole->jupyter)
  Downloading ipython_genutils-0.2.0-py2.py3-none-any.whl
Collecting traitlets (from qtconsole->jupyter)
  Downloading traitlets-4.3.2-py2.py3-none-any.whl (74kB)
    100% |████████████████████████████████| 81kB 1.6MB/s 
Collecting jupyter-client>=4.1 (from qtconsole->jupyter)
  Downloading jupyter_client-5.1.0-py2.py3-none-any.whl (84kB)
    100% |████████████████████████████████| 92kB 1.6MB/s 
Collecting jupyter-core (from qtconsole->jupyter)
  Downloading jupyter_core-4.3.0-py2.py3-none-any.whl (76kB)
    100% |████████████████████████████████| 81kB 1.3MB/s 
Collecting ipython (from jupyter-console->jupyter)
  Downloading ipython-6.1.0-py3-none-any.whl (741kB)
    100% |████████████████████████████████| 747kB 427kB/s 
Collecting prompt-toolkit<2.0.0,>=1.0.0 (from jupyter-console->jupyter)
  Downloading prompt_toolkit-1.0.14-py3-none-any.whl (248kB)
    100% |████████████████████████████████| 256kB 822kB/s 
Collecting testpath (from nbconvert->jupyter)
  Downloading testpath-0.3.1-py2.py3-none-any.whl (161kB)
    100% |████████████████████████████████| 163kB 1.4MB/s 
Collecting bleach (from nbconvert->jupyter)
  Downloading bleach-2.0.0-py2.py3-none-any.whl
Collecting jinja2 (from nbconvert->jupyter)
  Using cached Jinja2-2.9.6-py2.py3-none-any.whl
Collecting mistune!=0.6 (from nbconvert->jupyter)
  Downloading mistune-0.7.4-py2.py3-none-any.whl
Collecting nbformat (from nbconvert->jupyter)
  Downloading nbformat-4.3.0-py2.py3-none-any.whl (154kB)
    100% |████████████████████████████████| 163kB 1.2MB/s 
Collecting pandocfilters>=1.4.1 (from nbconvert->jupyter)
  Downloading pandocfilters-1.4.1.tar.gz
Collecting entrypoints>=0.2.2 (from nbconvert->jupyter)
  Downloading entrypoints-0.2.3-py2.py3-none-any.whl
Collecting widgetsnbextension~=2.0.0 (from ipywidgets->jupyter)
  Downloading widgetsnbextension-2.0.0-py2.py3-none-any.whl (1.1MB)
    100% |████████████████████████████████| 1.1MB 294kB/s 
Collecting tornado>=4.0 (from ipykernel->jupyter)
  Downloading tornado-4.5.1.tar.gz (483kB)
    100% |████████████████████████████████| 491kB 603kB/s 
Collecting terminado>=0.3.3; sys_platform != "win32" (from notebook->jupyter)
  Downloading terminado-0.6.tar.gz
Collecting six (from traitlets->qtconsole->jupyter)
  Using cached six-1.10.0-py2.py3-none-any.whl
Collecting decorator (from traitlets->qtconsole->jupyter)
  Downloading decorator-4.0.11-py2.py3-none-any.whl
Collecting python-dateutil>=2.1 (from jupyter-client>=4.1->qtconsole->jupyter)
  Using cached python_dateutil-2.6.0-py2.py3-none-any.whl
Collecting pyzmq>=13 (from jupyter-client>=4.1->qtconsole->jupyter)
  Downloading pyzmq-16.0.2-cp36-cp36m-manylinux1_i686.whl (2.9MB)
    100% |████████████████████████████████| 2.9MB 113kB/s 
Collecting pexpect; sys_platform != "win32" (from ipython->jupyter-console->jupyter)
  Downloading pexpect-4.2.1-py2.py3-none-any.whl (55kB)
    100% |████████████████████████████████| 61kB 2.7MB/s 
Collecting simplegeneric>0.8 (from ipython->jupyter-console->jupyter)
  Downloading simplegeneric-0.8.1.zip
Collecting jedi>=0.10 (from ipython->jupyter-console->jupyter)
  Downloading jedi-0.10.2-py2.py3-none-any.whl (190kB)
    100% |████████████████████████████████| 194kB 1.2MB/s 
Requirement already satisfied: setuptools>=18.5 in ./3.6.1/venv/jupyter/lib/python3.6/site-packages (from ipython->jupyter-console->jupyter)
Collecting pickleshare (from ipython->jupyter-console->jupyter)
  Downloading pickleshare-0.7.4-py2.py3-none-any.whl
Collecting wcwidth (from prompt-toolkit<2.0.0,>=1.0.0->jupyter-console->jupyter)
  Downloading wcwidth-0.1.7-py2.py3-none-any.whl
Collecting html5lib>=0.99999999 (from bleach->nbconvert->jupyter)
  Downloading html5lib-0.999999999-py2.py3-none-any.whl (112kB)
    100% |████████████████████████████████| 122kB 1.5MB/s 
Collecting MarkupSafe>=0.23 (from jinja2->nbconvert->jupyter)
  Using cached MarkupSafe-1.0.tar.gz
Collecting jsonschema!=2.5.0,>=2.4 (from nbformat->nbconvert->jupyter)
  Downloading jsonschema-2.6.0-py2.py3-none-any.whl
Collecting ptyprocess (from terminado>=0.3.3; sys_platform != "win32"->notebook->jupyter)
  Downloading ptyprocess-0.5.2-py2.py3-none-any.whl
Collecting webencodings (from html5lib>=0.99999999->bleach->nbconvert->jupyter)
  Downloading webencodings-0.5.1-py2.py3-none-any.whl
Installing collected packages: ptyprocess, pexpect, pygments, six, wcwidth, prompt-toolkit, simplegeneric, decorator, ipython-genutils, traitlets, jedi, pickleshare, ipython, python-dateutil, pyzmq, jupyter-core, jupyter-client, tornado, ipykernel, qtconsole, jupyter-console, testpath, webencodings, html5lib, bleach, MarkupSafe, jinja2, mistune, jsonschema, nbformat, pandocfilters, entrypoints, nbconvert, terminado, notebook, widgetsnbextension, ipywidgets, jupyter
  Running setup.py install for simplegeneric ... done
  Running setup.py install for tornado ... done
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for pandocfilters ... done
  Running setup.py install for terminado ... done
Successfully installed MarkupSafe-1.0 bleach-2.0.0 decorator-4.0.11 entrypoints-0.2.3 html5lib-0.999999999 ipykernel-4.6.1 ipython-6.1.0 ipython-genutils-0.2.0 ipywidgets-6.0.0 jedi-0.10.2 jinja2-2.9.6 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.1.0 jupyter-console-5.1.0 jupyter-core-4.3.0 mistune-0.7.4 nbconvert-5.2.1 nbformat-4.3.0 notebook-5.0.0 pandocfilters-1.4.1 pexpect-4.2.1 pickleshare-0.7.4 prompt-toolkit-1.0.14 ptyprocess-0.5.2 pygments-2.2.0 python-dateutil-2.6.0 pyzmq-16.0.2 qtconsole-4.3.0 simplegeneric-0.8.1 six-1.10.0 terminado-0.6 testpath-0.3.1 tornado-4.5.1 traitlets-4.3.2 wcwidth-0.1.7 webencodings-0.5.1 widgetsnbextension-2.0.0
```

#### 参考

* http://www.task-notes.com/entry/20151129/1448794509
* http://www.atmarkit.co.jp/ait/articles/1701/11/news013.html

