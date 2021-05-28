# **キーバリュー形式**で Java / Python / Node.js から IRIS にアクセスできるテンプレート（Native APIでのアクセスを体験できます）

このテンプレートでは、Java / Python / Node.js 用コンテナから InterSystems IRIS のコンテナへ接続し、**キーバリュー形式**でのデータ更新／取得を体験できます。

テンプレートの中では、以下の人物相関図のイメージを IRIS に登録しています。

**人物相関図のイメージ**
![](https://github.com/iijimam/doc-images/blob/master/IRIS-NativeAPI-Template/Relation.gif)

> テンプレートのテーマについて[ビデオによる解説](https://youtu.be/Yn3XYxXz16c)もあります。ぜひご参照ください。[開発者コミュニティ](https://jp.community.intersystems.com/)では、[こちらの記事](https://jp.community.intersystems.com/node/496871)でご紹介しています。

人物相関図と言えば、グラフデータベースをイメージされると思います。

IRIS はグラフデータベースではないのですが、IRIS ネイティブのデータの「**グローバル**」を利用することで、グラフデータベースと似たような構造を表現することができます。

> IRIS の高パフォーマンスを支える **「グローバル」** は 40 年以上前（＝ InterSystems 創業）から InterSystems のコア技術であるデータベースとして提供されてきました。 **「グローバル」** に対する操作方法は、現代のカテゴリに合わせるとしたら NoSQL データベースと言えます。

では、どのようにグラフデータベースのような構造を表現しているか？についてですが、グラフ構造は、ノードと辺から構成されていて、辺は 2 つのノードを結び付けるものです。

SNS の「友達」で考えると、ノードは「ユーザ」、辺は「友達関係」で表現できます。

テンプレートで使用している人物相関図では、ノードは「登場人物」、辺は「登場人物との関係」を表現しています。

**人物相関図のノードと辺（エッジ）**
![](https://github.com/iijimam/doc-images/blob/master/IRIS-NativeAPI-Template/Edge-Node.gif)


ノードと辺を、どのようにグローバル変数に設定しているでしょうか。


ノードは以下の通りです（配列には、画面表示に利用するノードの ID を設定し、右辺に人物名を登録しています）。
```
^Relation("Eren")="主人公（エレン）"
```

辺（エッジ）は以下の通りです（グローバル変数の配列を利用して、登場人物→関係のある人[ソース→ターゲット]を設定しています）。
>主人公エレンは、アルミン、ミカサ、ジークと関係がある。を表現しています。

```
^Relation("Eren","Armin")="" 
^Relation("Eren","Mikasa")=""
^Relation("Eren","Zeke")=""
```

両者で関係がある場合は、さらに以下のような配列を追加します。

```
^Relation("Mikasa")="エレンの幼馴染（ミカサ）"
^Relation("Mikasa","Armin")=""
^Relation("Mikasa","Eren")=""
```

実際に、IRIS サーバ側で記述する場合には、[ObjectScript](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_objectscript) の SET コマンドを使用してグローバル変数を設定します。

```
set ^Relation("Eren")="主人公（エレン）"
set ^Relation("Eren","Mikasa")=""
set ^Relation("Eren","Armin")=""
set ^Relation("Eren","Zeke")=""
set ^Relation("Mikasa")="エレンの幼馴染（ミカサ）"
set ^Relation("Mikasa","Armin")=""
set ^Relation("Mikasa","Eren")=""
```

配列のサブスクリプト（括弧の中身）は、配列のノード（例では、第 1 番目と第 2 番目）毎に Unicode 昇順でソートされます。

実行後、管理ポータルなどからグローバル変数一覧を参照すると、実行順に関係なく Unicode 昇順にソートされていることを確認できます。
> 管理ポータルは、[http://localhost:52779/csp/sys/UtilHome.csp](http://localhost:52779/csp/sys/UtilHome.csp) でアクセスできます（ユーザ名：_system　、パスワード：SYS）。

管理ポータル > [システムエクスプローラ] > [グローバル] > 左画面で「ネームスペース」USER を選択 > ^Relation の「表示」をクリック
![](https://github.com/iijimam/doc-images/blob/master/IRIS-NativeAPI-Template/MP-Global.gif)


ここまでご紹介したグローバル変数に対する各言語のコード例については、以下サブディレクトリをご参照ください。

- [Python](Python/README.md) ：jupyter のコンテナを用意します（Jupyter は 8896 ポートでアクセスできます）。
- [Node.js](Node.js/README.md)：Node 12 のコンテナを用意します（8080 ポートで確認用 Web ページを参照できます）。
- [Java](Java/README.md)：OpenJDK 8 のコンテナを用意します。


## 1) テンプレートの処理概要

テンプレートでは、Java / Python / Node.js 用から IRIS 用コンテナへ、キーバリュー形式でのアクセスを行うため、[Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) を使用しています。

> 各言語で必要な irisnative モジュールを使用するための手順は、言語ごとのサブディレクトリで解説しています。

- [Python](Python/README.md#1-テンプレートの処理概要) 
- [Node.js](Node.js/README.md#1-テンプレートの処理概要)
- [Java](Java/README.md#1-テンプレートの処理概要)


## 2) [Native API](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative) について

Native API は、IRIS 内部のネイティブデータ（＝グローバル変数）を直接操作できる API で [Java](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_dbnative)、[.NET](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_netnative)、[Python](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_pynative)、[Node.js](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_nodenative) からアクセスできます。
> グローバル変数の操作には、IRIS サーバーサイドプログラミングで使用する [ObjectScript](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_objectscript) を利用しますが、Native API を利用することで、[ObjectScript](https://docs.intersystems.com/irislatestj/csp/docbook/Doc.View.cls?KEY=AFL_objectscript) を使用せずにお好みの言語からアクセスすることができます。

また、Native API は、グローバル変数の設定／取得の他にも、クラスメソッド、ルーチン、関数を実行することができます。



## 3) テンプレートの使用方法

言語ごとのサブディレクトリにある README をご参照ください。

各言語のシンプルなサンプルコードの解説とコンテナの中身についての[ビデオによる説明](https://youtu.be/Yn3XYxXz16c)もあります。ぜひご参照ください。

- [Python](Python/README.md#2-テンプレートの使用方法) 
- [Node.js](Node.js/README.md#2-テンプレートの使用方法)
- [Java](Java/README.md#2-テンプレートの使用方法)



**READY SET CODE!!**