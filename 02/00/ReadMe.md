# [12.3. pip を使ったパッケージ管理](https://docs.python.jp/3/tutorial/venv.html#managing-packages-with-pip)

< [12. 仮想環境とパッケージ](https://docs.python.jp/3/tutorial/venv.html#virtual-environments-and-packages) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)


## [PyPI](https://pypi.python.org/pypi)

Python文書が日本語訳されていない……。

Pythonパッケージのストレージサーバ？pipからインストールするときに参照する場所と思われる。

## pip

pipはPythonパッケージ(ライブラリ)をインストールするツール。

古いPythonだと`easy_install`というツールがあったらしい。ネットの情報でもチラホラ見かける。しかし現在ではpipを使う。

## コマンド

前回の続き。仮想環境`tutorial-env`が有効な状態。そこでpipにてパッケージをインストールする。これにて仮想環境`tutorial-env`に指定パッケージをインストールしたことになる。

### 検索

`astronomy`パッケージを検索する。
```sh
(tutorial-env) $ pip search astronomy
```

### インストール

パッケージをインストールする。バージョン指定、最新版に更新できる。
```sh
(tutorial-env) $ pip install novas
(tutorial-env) $ pip install requests==2.6.0
(tutorial-env) $ pip install --upgrade requests
```

### アンインストール

```sh
(tutorial-env) $ pip uninstall novas
```

### パッケージの情報表示

```sh
(tutorial-env) $ pip show requests
```

### パッケージ一覧

```sh
(tutorial-env) $ pip list
```

### freeze

> インストールされたパッケージ一覧を、pip install が解釈するフォーマットで生成します。一般的な慣習として、このリストを requirements.txt というファイルに保存します

```sh
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

### install -r

> requirements.txt をバージョン管理システムにコミットして、アプリケーションの一部として配布することができます。ユーザーは必要なパッケージを install -r でインストールできます:

```sh
(tutorial-env) $ pip install -r requirements.txt
```

## ドキュメント

* https://docs.python.jp/3/installing/index.html#installing-index
* https://docs.python.jp/3/distributing/index.html#distributing-index

