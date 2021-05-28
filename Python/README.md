# **キーバリュー形式**で Python から IRIS にアクセスできる開発環境テンプレート（**Native API for Python**）

このテンプレートでは、Python 用コンテナ（Jupyter）から InterSystems IRIS のコンテナへ接続し、**キーバリュー形式**でのデータ更新／取得を体験できます。

[リポジトリの README](../README.md) でご紹介しているグローバル変数を Python から設定する場合のコードは以下の通りです。コード全体については [TryNativeAPI-host.py](/Python/TryNativeAPI-host.py) をご参照ください。
```
iris_native.set("主人公（エレン）","Relation","Eren")
iris_native.set(None,"Relation","Eren","Mikasa")
iris_native.set(None,"Relation","Eren","Armin")
iris_native.set(None,"Relation","Eren","Zeke")

iris_native.set("エレンの幼馴染（ミカサ）","Relation","Mikasa")
iris_native.set(None,"Relation","Mikasa","Armin")
iris_native.set(None,"Relation","Mikasa","Eren")
```


## 1) テンプレートの処理概要

開発環境テンプレートでは、Python 用コンテナ（Jupyter）から IRIS 用コンテナへ、キーバリュー形式でのアクセスを行うため、[Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) を使用しています。

Python から [Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) を使用するためには、irisnative モジュールのインポートが必要です。

モジュールは、[git](https://github.com/Intersystems-jp/IRISModules/tree/master/python/wheel) からダウンロードいただけますが、テンプレートでは手続きをまとめたコンテナとシェル（または batファイル）を用意しています。


>Python から IRIS へ接続する方法は 3 手法（JDBC／pyODBC／Native API）あります。pyODBC の利用方法については、[【はじめての InterSystems IRIS】セルフラーニングビデオ：アクセス編：Python から PyODBC を使って IRIS に接続してみよう](https://jp.community.intersystems.com/node/478616) をご参照ください。



## 2) テンプレートの使用方法

テンプレートはコンテナを利用しています。実行に必要なドライバは、コンテナビルド時に準備しています。

Docker、docker-compose、git が利用できる環境でお試しください。

**使用するコンテナのイメージ**
![](https://github.com/iijimam/doc-images2/blob/master/IRIS-NativeAPI-Template/conatiner-python.gif)
グラフ構造の確認には、Python の [networkx](https://networkx.org/) を使用しています。

また、データ登録後 [Cytoscape.js](https://js.cytoscape.org/) を利用した HTML でも人物相関を視覚的に確認できるようにしています。

[http://localhost:52779/csp/user/graph.html](http://localhost:52779/csp/user/graph.html)

> REST 経由でグローバル変数を取得しています。IRIS で作成する REST サーバについてご興味ある方は、ぜひ [こちらの記事](https://jp.community.intersystems.com/node/479546) もご参照ください。

HTML で特定の登場人物の関係者を探す場合は、クエリ文字列に人物名を指定してください（人物名は大小文字を区別します。先頭文字が大文字後は小文字で登録しています）。

 - 例1 [http://localhost:52779/csp/user/graph.html?Levi](http://localhost:52779/csp/user/graph.html?Levi)

 - 例2 [http://localhost:52779/csp/user/graph.html?Armin](http://localhost:52779/csp/user/graph.html?Armin)



サンプル実行までの手順は以下の通りです。

- [2-1) ダウンロード (git clone)](#2-1-ダウンロード-git-clone)
- [2-2) Python 用コンテナを使う場合](#2-2-Python-用コンテナを使う場合)

Python の実行をコンテナではなくてホストで行う場合は、以下手順をご参照ください。
- [3-1) Linuxの場合](#3-1-linuxの場合)
- [3-2) Windowsの場合](#3-2-windows-の場合)


### 2-1) ダウンロード (git clone)

```
git clone https://github.com/Intersystems-jp/IRIS-NativeAPI-Template.git
```


### 2-2) Python 用コンテナを使う場合

このフォルダ：[Python](.) にある [docker-compose.yml](docker-compose.yml) を使用します。

1) コンテナをビルドする方法

    ※ IRIS のイメージのダウンロードや Python 用コンテナの jupyter イメージのダウンロードやモジュールのインストールを行うため、少し時間がかかります。
    ```
    docker-compose build
    ```

2) コンテナを開始する方法

    ```
    docker-compose up -d
    ```

    
    - 停止したコンテナを再開する方法
        ```
        docker-compose start
        ```

3) サンプルを動かす方法（Jupyterを利用します）

    [http://localhost:8896/](http://localhost:8896/) にアクセスし、[TryNativeAPI.ipynb](jupyter-sample/TryNativeAPI.ipynb) を開きます（**ホスト名はご利用環境に合わせてご変更ください**）。

    コードのセルを選択し、Ctrl + Enter で実行するか、Cell > Run All を選択して実行してください。

    処理の流れは以下の通りです。

    - [1] irisnative パッケージのインポート（matplotlib と networkx もインポート）
    - [2] IRISに接続＋IRISオブジェクトの作成
    - [3] データ（^Relation）の作成
    - [4] [3]で設定した値を取得

    データを登録した後、登場人物の全関係者一覧します。
    
    その後、特定の登場人物の関係者を networkx を使用して表示します。

    **実行例（Jupyter）**
    ![](https://github.com/iijimam/doc-images2/blob/master/IRIS-NativeAPI-Template/Jupyter.gif)

   
4) コンテナを停止する方法
    

    ```
    docker-compose stop
    ```

    コンテナを**破棄したい場合**は **down** を指定して実行します。

    ```
    docker-compose down
    ```

5) Python 用コンテナのリビルド

    ※ 追加の Python モジュールをインストールしたい場合にコンテナのリビルドを行ってください）

    インストールしたいモジュール名を [requirements.txt](requirements.txt) に追記し（pip install 〇△ のモジュール名〇△ のみを追記してください。）以下実行します。
    
    ```
    docker-compose build jupyter
    ```


## 3) Python の実行をホストで行う場合

ホストに、Python 3 がインストールされている状態でお試し下さい。

ソースコードは、[TryNativeAPI-host.py](TryNativeAPI-host.py) にあります。

Python の 接続先 IRIS はコンテナの IRIS を使用しています。

IRIS の接続情報としてホスト名の指定があり、デフォルトは **localhost** が指定されていますが、実行環境に合わせて変更できるようにしています。

詳しくは [3-1) Linuxの場合](#3-1-linux%E3%81%AE%E5%A0%B4%E5%90%88)
 または [3-2) Windowsの場合](#3-2-windows-%E3%81%AE%E5%A0%B4%E5%90%88) ご参照ください。

サンプル実行結果として、以下のようなファイル（sample1.jpg）を出力します。実行後ご確認ください。
![](https://github.com/iijimam/doc-images2/blob/master/IRIS-NativeAPI-Template/sample1.jpg)


### 3-1) Linuxの場合

最初に、サンプルコードで使用しているモジュール（networkx、matplotlib、irisnative）をインストールするため、[pipinstall-linux.sh](pipinstall-linux.sh) を実行します。

```
~/IRIS-NativeAPI-Template$ cd Python
~/IRIS-NativeAPI-Template/Python$ ./pipinstall-linux.sh
```

Python の実行には、[runhost.sh](runhost.sh) を使用します。

**≪実行前にホスト名を確認してください≫**

Python から IRIS へ接続するときのホスト名に **localhost** を指定しています。

実行環境に合わせてホスト名を変更できるように、[host-params.sh](host-params.sh) にホスト名を指定し、環境変数に設定しています。

localhost 以外の場合は、[runhost.sh](runhost.sh) を実行する前に [host-params.sh](host-params.sh) の以下の行を環境に合わせて変更してください。

```
IRISHOSTNAME="localhost"
```

またサンプルでは、日本語表示を行うため、フォントに **TakaoPGothic** を指定しています。
他のフォントを指定する場合は、[host-params.sh](host-params.sh) の以下の行を修正してください。

```
SAMPLEFONT="TakaoPGothic"
```

事前準備ができたら、[runhost.sh](runhost.sh) を実行します。

実行例）
データ登録後、登場人物の全関係者を文字で出力します。その後、特定の登場人物の関係者を networkx を使用
した表示で確認できます（ファイル出力します）。

```
~/IRIS-NativeAPI-Template/Python$ ./runhost.sh
Armin - エレンの幼馴染
（アルミン）
  関係者： Bertolt
  関係者： Eren
  関係者： Mikasa
Bertolt - 超大型の巨人
（ベルトルト）
  関係者： Reiner
  ＜省略＞
******************************
Leviに関連する人物を探します
******************************

networkxの表示を sample1.jpg　に出力しました
----------------------
** 処理終了しました **
----------------------
~IRIS-NativeAPI-Template/Python$
```


### 3-2) Windows の場合

最初に、サンプルコードで使用しているモジュール（networkx、matplotlib、irisnative）をインストールするため、[pipinstall.bat](pipinstall.bat) を実行します。

```
~/IRIS-NativeAPI-Template> cd Python
~/IRIS-NativeAPI-Template/Python> pipinstall.bat
```

Python の実行には、[runhost.bat](runhost.bat) を使用します。

**≪実行前にホスト名を確認してください≫**

Python から IRIS へ接続するときのホスト名に **localhost** を指定しています。

実行環境に合わせてホスト名を変更できるように、[host-params.bat](host-params.bat) にホスト名を指定し、環境変数に設定しています。

localhost 以外の場合は、[runhost.bat](runhost.bat) を実行する前に [host-params.bat](host-params.bat) の以下行を環境に合わせて変更してください。

```
SET IRISHOSTNAME=localhost
```

またサンプルでは、日本語表示を行うため、フォントに **MS Gothic** を指定しています。
他のフォントを指定する場合は、[host-params.bat](host-params.bat) の以下の行を修正してください。

```
SET SAMPLEFONT=MS Gothic
```

事前準備ができたら、[runhost.bat](runhost.bat) を実行します。

実行例）
データ登録後、登場人物の全関係者を文字で出力します。その後、特定の登場人物の関係者を networkx を使用
した表示で確認できます（ファイル出力します）。

```
~/IRIS-NativeAPI-Template/Python> runhost.bat
Armin - エレンの幼馴染
（アルミン）
  関係者： Bertolt
  関係者： Eren
  関係者： Mikasa
Bertolt - 超大型の巨人
（ベルトルト）
  関係者： Reiner
    ＜省略＞

******************************
Leviに関連する人物を探します
******************************

networkxの表示を sample1.jpg　に出力しました
-----------------------
 ** completed !! **
-----------------------

>
```

**READY SET CODE!!**