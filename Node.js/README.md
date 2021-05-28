# **キーバリュー形式**で Node.js から IRIS にアクセスできる開発環境テンプレート（**Native API for Node.js**）

このテンプレートでは、Node.js 用コンテナから InterSystems IRIS のコンテナへ接続し、**キーバリュー形式**でのデータ更新／取得を体験できます。

[リポジトリの README](../README.md) でご紹介しているグローバル変数を Node.js から設定する場合のコードは以下の通りです。コードについては [NativeAPITest.js](NativeAPITest.js) をご参照ください。
```
iris_native.set("主人公（エレン）","Relation","Eren")
iris_native.set(null,"Relation","Eren","Mikasa")
iris_native.set(null,"Relation","Eren","Armin")
iris_native.set(null,"Relation","Eren","Zeke")

iris_native.set("エレンの幼馴染（ミカサ）","Relation","Mikasa")
iris_native.set(null,"Relation","Mikasa","Armin")
iris_native.set(null,"Relation","Mikasa","Eren")
```


## 1) テンプレートの処理概要

開発環境テンプレートでは、Node.js 用コンテナから IRIS 用コンテナへ、キーバリュー形式でのアクセスを行うため、[Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) を使用しています。

Node.js から [Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) を使用するためには、irisnative モジュールのインポートが必要です。

irisnative 用モジュールは、[git](https://github.com/Intersystems-jp/IRISModules) からダウンロードいただけますが、テンプレートでは手続きをまとめたコンテナとシェル（または batファイル）を用意しています。


## 2) テンプレートの使用方法

テンプレートはコンテナを利用しています。実行に必要なドライバは、コンテナビルド時に準備しています。

Docker、docker-compose、git が利用できる環境でお試しください。

**使用するコンテナのイメージ**
![](https://github.com/iijimam/doc-images2/blob/master/IRIS-NativeAPI-Template/conatiner-node.gif)

データ登録後 [Cytoscape.js](https://js.cytoscape.org/) を利用した HTML でも人物相関を視覚的に確認できるようにしています。

[http://localhost:8080](http://localhost:8080)

> REST 経由でグローバル変数を取得しています。IRIS で作成する REST サーバについてご興味ある方は、ぜひ [こちらの記事](https://jp.community.intersystems.com/node/479546) もご参照ください。

HTML で特定の登場人物の関係者を探す場合は、クエリ文字列に人物名を指定してください（人物名は大小文字を区別します。先頭文字が大文字後は小文字で登録しています）。

 - 例1 [http://localhost:8080?Levi](http://localhost:8080?Levi)

 - 例2 [http://localhost:8080?Armin](http://localhost:8080?Armin)



サンプル実行までの手順は以下の通りです。

- [2-1) ダウンロード (git clone)](#2-1-ダウンロード-git-clone)
- [2-2) Node.js 用コンテナを使う場合](#2-2-nodejs-用コンテナを使う場合)

Node.js の実行をコンテナではなくてホストで行う場合は、以下手順をご参照ください。
- [3-1) Linuxの場合](#3-1-linuxの場合)
- [3-2) Windowsの場合](#3-2-windows-の場合)

コンテナの Node.js の開発環境を自由にご利用いただくこともできます。詳細は以下ご参照ください。
- [4) 新規作成したファイルを実行する方法](#4-新規作成したファイルを実行する方法)

### 2-1) ダウンロード (git clone)

```
git clone https://github.com/Intersystems-jp/IRIS-NativeAPI-Template.git
```


### 2-2) Node.js 用コンテナを使う場合

このフォルダ：[Node.js](.) にある [docker-compose.yml](docker-compose.yml) を使用します。

1) コンテナをビルドする方法

    ※ IRIS のイメージのダウンロードや Node.js 用コンテナのイメージのダウンロードやモジュールのインストールを行うため、少し時間がかかります。
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

3) サンプルを動かす方法
        ```
        docker-compose run nodejs node NativeAPITest.js
        ```

    データを登録した後、登場人物の全関係者一覧します。
    
    その後、特定の登場人物の関係者一覧します。
    
    実行例は以下の通りです。
    ```
    ~IRIS-NativeAPI-Template/Node.js$ docker-compose run nodejs node NativeAPITest.js
    Creating iris-nativeapi-nodejs-template_nodejs_run ... done

    ****　第1ノードに登録された人の関係者を全件表示します　****
    source-エレンの幼馴染（アルミン）
      関係者： Bertolt
      関係者： Eren
      関係者： Mikasa
    ＜-- 表示省略 --＞
    ==================================================================
    管理ポータル > システムエクスプローラー > グローバル
    接続したネームスペースに切り替え ^Relation を参照してください
    ==================================================================

    指定した人物の関係者を探します。人物名を入力（Armin、Levi、Zeke など） >>Levi

    Levi の関係者を探します
      関係者： Zeke

    Zeke の関係者を探します
      関係者： Eren

    Eren の関係者を探します
      関係者： Armin
      関係者： Mikasa
      関係者： Zeke

    **** 終わり ****

    ~IRIS-NativeAPI-Template/Node.js$    
    ```
   
4) コンテナを停止する方法
    

    ```
    docker-compose stop
    ```

    コンテナを**破棄したい場合**は **down** を指定して実行します。

    ```
    docker-compose down
    ```

5) Node.js 用コンテナのリビルド

    ※ [ソースコード](src)を修正した場合、コンテナのリビルドを行ってください。
    
    ```
    docker-compose build nodejs
    ```


## 3) Node.js の実行をホストで行う場合

ホストに、Node.js がインストールされている状態でお試し下さい。

ソースコードは、[NativeAPITest.js](./src/NativeAPITest.js) にあります。

Node.js の 接続先 IRIS はコンテナの IRIS を使用しています。

[2-2) Node.js 用コンテナを使う場合](#2-2-nodejs-用コンテナを使う場合) でコンテナで試されている場合は、一旦コンテナを破棄し、IRIS のコンテナのみ開始します。

```
docker-compose down
docker-compose up -d iris
```

IRIS の接続情報としてホスト名の指定があり、デフォルトは **localhost** が指定されていますが、実行環境に合わせて変更できるようにしています。

詳しくは [3-1) Linuxの場合](#3-1-linux%E3%81%AE%E5%A0%B4%E5%90%88)
または [3-2) Windowsの場合](#3-2-windows-%E3%81%AE%E5%A0%B4%E5%90%88) ご参照ください。


### 3-1) Linuxの場合

最初に、サンプルコードで使用しているモジュール（express、irisnative）をインストールするため、[nominstall.sh](npminstall.sh) を実行します。

```
~/IRIS-NativeAPI-Template$ cd Node.js
~/IRIS-NativeAPI-Template/Node.js$ ./npminstall.sh
```

Node.js の実行には、[runhost.sh](runhost.sh) を使用します。

**≪実行前にホスト名を確認してください≫**

Node.js から IRIS へ接続するときのホスト名に **localhost** を指定しています。

実行環境に合わせてホスト名を変更できるように、[host-params.sh](host-params.sh) にホスト名を指定し、環境変数に設定しています。

localhost 以外の場合は、[runhost.sh](runhost.sh) を実行する前に [host-params.sh](host-params.sh) の以下の行を環境に合わせて変更してください。

```
IRISHOSTNAME="localhost"
```

事前準備ができたら、[runhost.sh](runhost.sh) を実行します。

実行例）
データ登録後、登場人物の全関係者を文字で出力します。その後、特定の登場人物の関係者を networkx を使用
した表示で確認できます（ファイル出力します）。

```
~/IRIS-NativeAPI-Template/Node.js$ ./runhost.sh

****　第1ノードに登録された人の関係者を全件表示します　****
source-エレンの幼馴染（アルミン）
   関係者： Bertolt
   関係者： Eren
   関係者： Mikasa
source-超大型の巨人（ベルトルト）
   関係者： Reiner
source-エレンのお母さん（カルラ）：ダイナに捕食
   関係者： Grisha
  ≪表示省略≫
==================================================================
管理ポータル > システムエクスプローラー > グローバル
 接続したネームスペースに切り替え ^Relation を参照してください
==================================================================
指定した人物の関係者を探します。人物名を入力（Armin、Levi、Zeke など） >>Armin

Armin の関係者を探します
   関係者： Bertolt
   関係者： Eren
   関係者： Mikasa

Bertolt の関係者を探します
   関係者： Reiner

Reiner の関係者を探します
   関係者： Bertolt

  ≪表示省略≫
 **** 終わり ****

Running at Port 8080...

http://localhost:8080/ にアクセスするとグラフ構造をHTMLで確認できます。
※ ホスト名は環境に合わせて変更してください ※

Ctrl + C で終了します。

```

実行が完了すると、IRIS にデータが登録されるので、HTML で確認できます。

[http://localhost:8080](http://localhost:8080)

**ホスト名は環境に合わせて変更してください**


### 3-2) Windows の場合

最初に、サンプルコードで使用しているモジュール（express、irisnative）をインストールするため、[npminstall.bat](npminstall.bat) を実行します。

```
~/IRIS-NativeAPI-Template> cd Node.js
~/IRIS-NativeAPI-Template/Node.js> npminstall.bat
```

Node.js の実行には、[runhost.bat](runhost.bat) を使用します。

**≪実行前にホスト名を確認してください≫**

Node.js から IRIS へ接続するときのホスト名に **localhost** を指定しています。

実行環境に合わせてホスト名を変更できるように、[host-params.bat](host-params.bat) にホスト名を指定し、環境変数に設定しています。

localhost 以外の場合は、[runhost.bat](runhost.bat) を実行する前に [host-params.bat](host-params.bat) の以下行を環境に合わせて変更してください。

```
SET IRISHOSTNAME=localhost
```

事前準備ができたら、[runhost.bat](runhost.bat) を実行します。

実行例）
データ登録後、登場人物の全関係者を文字で出力します。その後、特定の登場人物の関係者を networkx を使用
した表示で確認できます（ファイル出力します）。

```
~/IRIS-NativeAPI-Template/NodeJS> runhost.bat

****　第1ノードに登録された人の関係者を全件表示します　****
source-エレンの幼馴染（アルミン）
   関係者： Bertolt
   関係者： Eren
   関係者： Mikasa
source-超大型の巨人（ベルトルト）
   関係者： Reiner
source-エレンのお母さん（カルラ）：ダイナに捕食
   関係者： Grisha
  ≪表示省略≫
==================================================================
管理ポータル > システムエクスプローラー > グローバル
 接続したネームスペースに切り替え ^Relation を参照してください
==================================================================
指定した人物の関係者を探します。人物名を入力（Armin、Levi、Zeke など） >>Armin

Armin の関係者を探します
   関係者： Bertolt
   関係者： Eren
   関係者： Mikasa

Bertolt の関係者を探します
   関係者： Reiner

Reiner の関係者を探します
   関係者： Bertolt

  ≪表示省略≫
 **** 終わり ****

Running at Port 8080...

http://localhost:8080/ にアクセスするとグラフ構造をHTMLで確認できます。
※ ホスト名は環境に合わせて変更してください ※

Ctrl + C で終了します。

>
```

実行が完了すると、IRIS にデータが登録されるので、HTML で確認できます。

[http://localhost:8080](http://localhost:8080)

**ホスト名は環境に合わせて変更してください**


## 4) 新規作成したファイルを実行する方法

[docker-compose.yml](docker-compose.yml) では、Node.js コンテナ内の /usr/projects/ISC ディレクトリをホストの [ISC](ISC) にマウントしているので、新規作成したファイルを git clone 後にできるディレクトリ（IRIS-NativeAPI-Template）以下の Node.js/ISC に配置いただくことで、Node.js の実行を確認できます。

テスト用ファイル [test.js](ISC/test.js) を実行する場合は以下の通りです。

```
~IRIS-NativeAPI-Template/Node.js$ docker-compose run nodejs node ISC/test.js
Creating iris-nativeapi-nodejs-template_nodejs_run ... done
こんにちは
~IRIS-NativeAPI-Template/Node.js$
```

※ IRIS と Node.js のコンテナが開始している必要があります。詳細は [2-2) Node.js 用コンテナを使う場合](#2-2-nodejs-用コンテナを使う場合) をご参照ください。


**READY SET CODE!!**