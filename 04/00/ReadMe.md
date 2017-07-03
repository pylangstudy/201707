# [16.1. 対話モード](https://docs.python.jp/3/tutorial/appendix.html#interactive-mode) 

< [16. 付録](https://docs.python.jp/3/tutorial/appendix.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

短いので複数項目を終わらせる。

## [16.1.1. エラー処理](https://docs.python.jp/3/tutorial/appendix.html#error-handling)

> エラーが発生すると、インタプリタはエラーメッセージとスタックトレース (stack trace) を出力します。対話モードにいるときは、インタプリタは一次プロンプトに戻ります; スクリプトをファイルから実行しているときは、インタプリタはスタックトレースを出力した後、非ゼロの終了ステータスで終了します。 (try 文の except 節で処理された例外は、ここでいうエラーにはあたりません。) いくつかのエラーは常に致命的であり、非ゼロの終了ステータスとなるプログラムの終了を引き起こします。例えばインタプリタ内部の矛盾やある種のメモリ枯渇が当てはまります。エラーメッセージは全て標準エラー出力に書き込まれます; これに対して、通常は実行した命令から出力される内容は標準出力に書き込まれます。

> 割り込み文字 (interrupt character、普通は Control-C か Delete) を一次または二次プロンプトに対してタイプすると、入力が取り消されて一次プロンプトに戻ります。 [1] コマンドの実行中に割り込み文字をタイプすると KeyboardInterrupt 例外が送出されます。この例外は try 文で処理できます。

エラーについては[8. エラーと例外](https://docs.python.jp/3/tutorial/errors.html)でやった。

## [16.1.2. 実行可能な Python スクリプト](https://docs.python.jp/3/tutorial/appendix.html#executable-python-scripts)

> BSD 風の Unix システムでは、Python スクリプトはシェルスクリプトのように直接実行可能にできます。

```python
#!/usr/bin/env python3.5
```

> (ここではインタプリタがユーザの PATH 上にあると仮定しています) をスクリプトの先頭に置き、スクリプトファイルに実行可能モードを設定します。 #! はファイルの最初の２文字でなければなりません。プラットフォームによっては、この最初の行を終端する改行文字が Windows 形式 ('\r\n') ではなく、 Unix形式('\n')でなければならないことがあります。ハッシュまたはポンド文字、すなわち '#' は、Python ではコメントを書き始めるために使われていることに注意してください。

`#!`というのはHashbang、略してShebangなどと呼ばれるものらしい。

> chmod コマンドを使えば、スクリプトに実行モードや実行権限を与えることができます。

```sh
$ chmod +x myscript.py
```

### 実行ファイル作成手順

１．Pythonコマンドのパスを取得する（Linuxでは`which`コマンドで指定したコマンドののパスを調べることが可能）
```sh
$ which python3
/usr/bin/python3
```

２．`0.py`を作成する
```python
#!/usr/bin/python3
print('Hello 0.py!!')
```

３．実行権限を与える
```sh
$ chmod +x 0.py
```

４．実行する
```sh
$ ./0.py
Hello 0.py!!
```

## [16.1.3. 対話モード用の起動時実行ファイル](https://docs.python.jp/3/tutorial/appendix.html#the-interactive-startup-file)

### PYTHONSTARTUP

> Python を対話的に使うときには、インタプリタが起動する度に実行される何らかの標準的なコマンドがあると便利なことがよくあります。これを行うには、 PYTHONSTARTUP と呼ばれる環境変数を、インタプリタ起動時に実行されるコマンドが入ったファイル名に設定します。この機能は Unix シェルの .profile に似ています。

> このファイルは対話セッションのときだけ読み出されます。 Python がコマンドをスクリプトから読み出しているときや、 /dev/tty がコマンドの入力元として明示的に指定されている(この場合対話的セッションのように動作します) わけではない 場合にはこのファイルは読み出されません。ファイル内のコマンドは、対話的コマンドが実行される名前空間と同じ名前空間内で実行されます。このため、ファイル内で定義されていたり import されたオブジェクトは、そのまま対話セッション内で使うことができます。また、このファイル内で sys.ps1 や sys.ps2 を変更して、プロンプトを変更することもできます。

> もし現在のディレクトリから追加でスタートアップファイルを読み出したいのなら、グローバルのスタートアップファイルの中に if os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read()) のようなプログラムを書くことができます。スクリプト中でスタートアップファイルを使いたいのなら、以下のようにしてスクリプト中で明示的に実行しなければなりません:

```python
import os
filename = os.environ.get('PYTHONSTARTUP')
print(filename)
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)
```
```sh
$ python3 1.py
None
```

最初は何もないらしい。ソースコードから察するに、PYTHONSTARTUPには1つのファイルパスを指定するようだ。とくに用途が思いつかないのでスルー。

## [16.1.4. カスタマイズ用モジュール](https://docs.python.jp/3/tutorial/appendix.html#the-customization-modules)

> Python はユーザーが Python をカスタマイズするための2つのフック、 sitecustomize と usercustomize を提供しています。これがどのように動作しているかを知るには、まずはユーザーの site-packages ディレクトリの場所を見つける必要があります。Python を起動して次のコードを実行してください:

```sh
$ python3 2.py 
/home/{user}/.local/lib/python3.6/site-packages
```

> usercustomize.py をそのディレクトリに作成して、そこでやりたいことをすべて書くことができます。このファイルは自動インポートを無効にする -s オプションを使わない限り、全ての Python の起動時に実行されます。

> sitecustomize モジュールも同じように動作しますが、一般的にコンピューターの管理者によって、グローバルの site-packages ディレクトリに作成され、 usercustomize より先にインポートされます。詳細は site モジュールのドキュメントを参照してください。

仮想環境の有効化コマンドを実行するなどで使えるだろうか？しかし環境は都度選びたい。これまた用途が思いつかない。

## 完

これにて[チュートリアル](https://docs.python.jp/3/tutorial/index.html)完了。

