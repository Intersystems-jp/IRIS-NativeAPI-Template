# **キーバリュー形式**で Java から IRIS にアクセスできる実行環境テンプレート（**NativeAPI for Java**）

このテンプレートでは、Java の実行環境用コンテナから InterSystems IRIS のコンテナへ接続し、**キーバリュー形式**でのデータ更新／取得を体験できます。


[リポジトリの README](../README.md) でご紹介しているグローバル変数を Java から設定する場合のコードは以下の通りです。コード全体については [Start.java](NativeAPI/Start.java) をご参照ください。
```
irisNative.set("主人公（エレン）","Relation","Eren");
irisNative.set("","Relation","Eren","Mikasa");
irisNative.set("","Relation","Eren","Armin");
irisNative.set("","Relation","Eren","Zeke");

irisNative.set("エレンの幼馴染（ミカサ）","Relation","Mikasa");
irisNative.set("","Relation","Mikasa","Armin");
irisNative.set("","Relation","Mikasa","Eren");
```


## 1) テンプレートの処理概要

実行環境テンプレートでは、Java 用コンテナから IRIS 用コンテナへ、キーバリュー形式でのアクセスを行うため、[Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) を使用しています。
[Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) は、IRIS の JDBC ドライバを使用してアクセスできます。

> Java から IRIS へ接続する方法は 4 手法（JDBC／XEP／Native API／Hibernate）あります。XEP（大量データの高速登録に最適な方法）をお試しいただける実行環境テンプレートをご用意しています。ご興味ありましたら、[GPS（GPX）データを InterSystems IRIS に高速に取り込む方法を体験できる実行環境テンプレート](https://jp.community.intersystems.com/node/495076) をご参照ください。


## 2) 実行環境テンプレートの使用方法

実行環境テンプレートはコンテナを利用しています。実行に必要なドライバは、コンテナビルド時に準備しています。

Docker、docker-compose、git が利用できる環境でお試しください。

**使用するコンテナのイメージ**
![](https://github.com/iijimam/doc-images/blob/master/IRIS-NativeAPI-Template/conatiner.gif)

Java からデータ登録後、[Cytoscape.js](https://js.cytoscape.org/) を利用した HTML を使用して人物相関を視覚的に確認できます。


[http://localhost:52779/csp/user/graph.html](http://localhost:52779/csp/user/graph.html)

> REST 経由でグローバル変数を取得しています。IRIS で作成する REST サーバについてご興味ある方は、ぜひ [こちらの記事](https://jp.community.intersystems.com/node/479546) もご参照ください。

登場人物を特定して関係者を探す場合は、クエリ文字列に人物名を指定してください（人物名は大小文字を区別します。先頭文字が大文字後は小文字で登録しています）。

 - 例1 [http://localhost:52779/csp/user/graph.html?Levi](http://localhost:52779/csp/user/graph.html?Levi)

 - 例2 [http://localhost:52779/csp/user/graph.html?Armin](http://localhost:52779/csp/user/graph.html?Armin)

**※ ホスト名は操作環境に合わせて変更してください ※**


実行手順は以下の通りです。

- [2-1) ダウンロード (git clone)](#2-1-%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89-git-clone)
- [2-2) Java実行環境用コンテナを使う場合](#2-2-java%E5%AE%9F%E8%A1%8C%E7%92%B0%E5%A2%83%E7%94%A8%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88)

Java の実行をコンテナではなくてホストで行う場合は、以下手順をご参照ください。
- [3-1) Linuxの場合](#3-1-linux%E3%81%AE%E5%A0%B4%E5%90%88)
- [3-2) Windowsの場合](#3-2-windows-%E3%81%AE%E5%A0%B4%E5%90%88)


### 2-1) ダウンロード (git clone)

```
git clone https://github.com/Intersystems-jp/IRIS-NativeAPI-Template.git
```


### 2-2) Java実行環境用コンテナを使う場合

このフォルダ：[Java](.) にある [docker-compose.yml](docker-compose.yml) を使用します。

1) コンテナをビルドする方法

    ※ IRIS のイメージのダウンロードや Java 実行環境の作成を行うため、少し時間がかかります。
    ```
    docker-compose build
    ```

2) コンテナを開始する方法

    ```
    docker-compose up -d iris
    ```
    この実行で **IRIS 用コンテナ** が開始します（Java 用コンテナは Java 実行時に開始します）。

    
    - 停止したコンテナを再開する方法（Java 用コンテナは Java 実行時に開始します）。
        ```
        docker-compose start iris
        ```

3) サンプルを動かす方法

    データを登録した後、登場人物の全関係者を表示します。
    
    その後、画面で登場人物名を入力すると、指定した人物の関係者を画面表示します。
    
    ```
    $ docker-compose run java
    Creating iris-nativeapi-java-template_java_run ... done
    InterSystemsIRISにJDBC経由で接続できました
    ****^Relation(第1ノード) に登録された人の関係者を全件表示します *****

    人物 = Armin - 説明：エレンの幼馴染（アルミン）
    関係者 : Bertolt
    関係者 : Eren
    関係者 : Mikasa

    人物 = Bertolt - 説明：超大型の巨人（ベルトルト）
        <省略>

    IRISの管理ポータルで ^Relation のデータを確認してください

    指定した人物の関係者を探します。人物名を入力（Eren、Levi、Zeke など） >>Zeke

    Zeke の関係者を探します
    関係者 : Eren

    Eren の関係者を探します
    関係者 : Armin
        <省略>
    $
    ```
4) コンテナを停止する方法
    

    ```
    docker-compose stop
    ```

    IRIS／Java のコンテナを**破棄したい場合**は **down** を指定して実行します。

    ```
    docker-compose down
    ```

5) Javaのソースコードを変えた場合の反映方法
    
    ```
    docker-compose build java
    ```


## 3) Java の実行をホストで行う場合

ホストに、OpenJDK 8 がインストールされている状態でお試し下さい。

ソースコードは、[NativeAPI/Start.java](NativeAPI/Start.java) にあります。

Java の 接続先 IRIS はコンテナの IRIS を使用しています。

### 3-1) Linuxの場合

Java から IRIS へ接続するときのホスト名に **localhost** を指定しています。

実行環境に合わせてホスト名を変更できるように、[host-java-params.sh](host-java-params.sh) にホスト名を指定し、環境変数に設定しています。

localhost 以外の場合は、以降に登場するシェル実行前に [host-java-params.sh](host-java-params.sh) の以下行を環境に合わせて変更してください。

```
IRISHOSTNAME="localhost"
```

準備ができたら以下の手順で実行してください。


```
~/IRIS-NativeAPI-Template$ cd Java
~/IRIS-NativeAPI-Template/Java$ source ./host-java-params.sh
~/IRIS-NativeAPI-Template/Java$ ./build-java-host.sh           
```

Javaの実行には、[runhost.sh](runhost.sh) を使用します。

データを登録した後、登場人物の全関係者を表示します。
その後、画面で登場人物名を入力すると、指定した人物の関係者を画面表示します。

実行例）
```
~IRIS-NativeAPI-Template/Java$ ./runhost.sh
InterSystemsIRISにJDBC経由で接続できました
****^Relation(第1ノード) に登録された人の関係者を全件表示します *****

人物 = Armin - 説明：エレンの幼馴染（アルミン）
   関係者 : Bertolt
   関係者 : Eren
   関係者 : Mikasa

人物 = Bertolt - 説明：超大型の巨人（ベルトルト）
   関係者 : Reiner
     ＜表示省略＞
IRISの管理ポータルで ^Relation のデータを確認してください

指定した人物の関係者を探します。人物名を入力（Armin、Levi、Zeke など） >>Levi

Levi の関係者を探します
   関係者 : Zeke

Zeke の関係者を探します
   関係者 : Eren

Eren の関係者を探します
   関係者 : Armin
   関係者 : Mikasa
   関係者 : Zeke
----------------------
** 処理終了しました **
----------------------
~IRIS-NativeAPI-Template/Java$    
```

### 3-2) Windows の場合

Java から IRIS へ接続するときのホスト名に **localhost** を指定しています。

実行環境に合わせてホスト名を変更できるように、[host-java-params.bat](host-java-params.bat) にホスト名を指定し、環境変数に設定しています。

localhost 以外の場合は、以降に登場するシェル実行前に [host-java-params.bat](host-java-params.bat) の以下行を環境に合わせて変更してください。

```
SET IRISHOSTNAME=localhost
```

準備ができたら以下の手順で実行してください。

```
~/IRIS-NativeAPI-Template> cd Java
~/IRIS-NativeAPI-Template/Java> host-java-params.bat
~/IRIS-NativeAPI-Template/Java> build-java-host.bat           
```

Javaの実行には、[runhost.bat](runhost.bat) を使用します。

データを登録した後、登場人物の全関係者を表示します。
その後、画面で登場人物名を入力すると、指定した人物の関係者を画面表示します。

実行例）
```
~/IRIS-NativeAPI-Template/Java> runhost.bat
InterSystemsIRISにJDBC経由で接続できました
****^Relation(第1ノード) に登録された人の関係者を全件表示します *****

人物 = Armin - 説明：エレンの幼馴染（アルミン）
   関係者 : Bertolt
   関係者 : Eren
   関係者 : Mikasa

人物 = Bertolt - 説明：超大型の巨人（ベルトルト）
   関係者 : Reiner
    ＜表示省略＞
IRISの管理ポータルで ^Relation のデータを確認してください

指定した人物の関係者を探します。人物名を入力（Armin、Levi、Zeke など） >>Levi

Levi の関係者を探します
   関係者 : Zeke

Zeke の関係者を探します
   関係者 : Eren

Eren の関係者を探します
   関係者 : Armin
   関係者 : Mikasa
   関係者 : Zeke
-----------------------
 ** completed !! **
-----------------------
~/IRIS-NativeAPI-Template/Java>     
```


**READY SET CODE!!**