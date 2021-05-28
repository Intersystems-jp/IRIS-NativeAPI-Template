#!/usr/local/bin/python
# coding:utf-8

#InterSystems IRIS の Python Native APIを使ってみよう
######################################
#[1] irisnative パッケージのインポート
#[2] IRISに接続＋IRISオブジェクトの作成
#[3] ^Relationの作成
#[4] [3]で設定した値の取得
######################################

#[1] irisnative パッケージのインポート
import irisnative
import networkx as nx
import matplotlib.pyplot as plt

import os

G=nx.DiGraph()

def getRelation(source,graph,count):
    if count>3:
        return

    #ラベル表示用のデータ取得
    labellist[source]=iris_native.get("Relation",source)

    iter = iris_native.iterator("Relation",source)
    nodelist=[source for source in iter.subscripts() ]
    edgelist=[(source,target) for target in nodelist]
    graph.add_nodes_from(nodelist)
    graph.add_edges_from(edgelist)

    for target in nodelist:
        #ラベル表示用のデータ取得
        labellist[target]=iris_native.get("Relation",target)
        getRelation(target,graph,count+1)


#[2]IRISに接続＋IRISオブジェクトの作成

# 接続ホスト名を環境変数から取得。ない場合は localhost
host=os.environ.get('IRISHOSTNAME')

if host ==None:
    host = "localhost"

connection = irisnative.createConnection(host,1972,"user","_system","SYS")
iris_native = irisnative.createIris(connection)

#[3] 登場人物の登録
#   set ^Relation("Eren")="主人公（エレン）
iris_native.set("主人公\n（エレン）","Relation","Eren")
iris_native.set("エレンの幼馴染\n（アルミン）","Relation","Armin")
iris_native.set("エレンの幼馴染\n（ミカサ）","Relation","Mikasa")
iris_native.set("エレンのお父さん\n（グリシャ）","Relation","Grisha")
iris_native.set("エレンの異母兄弟\n（ジーク）","Relation","Zeke")
iris_native.set("鎧の巨人\n（ライナー）","Relation","Reiner")
iris_native.set("超大型の巨人\n（ベルトルト）","Relation","Bertolt")
iris_native.set("エレンのお母さん（カルラ）\nダイナに捕食","Relation","Carla")
iris_native.set("ジークのお母さん（ダイナ）\nレイス王家[フリッツ家]","Relation","Dina")
iris_native.set("人類最強の兵士\n（リヴァイ）","Relation","Levi")

#関係性を設定
#   set ^Relation("Eren","Mikasa")=""
iris_native.set(None,"Relation","Eren","Mikasa")
iris_native.set(None,"Relation","Eren","Armin")
iris_native.set(None,"Relation","Armin","Mikasa")
iris_native.set(None,"Relation","Mikasa","Armin")
iris_native.set(None,"Relation","Armin","Eren")
iris_native.set(None,"Relation","Mikasa","Eren")
iris_native.set(None,"Relation","Grisha","Eren")
iris_native.set(None,"Relation","Grisha","Zeke")
iris_native.set(None,"Relation","Eren","Zeke")
iris_native.set(None,"Relation","Zeke","Eren")
iris_native.set(None,"Relation","Grisha","Dina")
iris_native.set(None,"Relation","Dina","Grisha")           
iris_native.set(None,"Relation","Grisha","Carla")
iris_native.set(None,"Relation","Carla","Grisha")
iris_native.set(None,"Relation","Dina","Carla")
iris_native.set(None,"Relation","Armin","Bertolt")
iris_native.set(None,"Relation","Reiner","Bertolt")
iris_native.set(None,"Relation","Bertolt","Reiner")
iris_native.set(None,"Relation","Levi","Zeke")

#[4] 全件取得
for source,value in iris_native.iterator("Relation").items():
    print(source,"-",value)

    for target,value in iris_native.iterator("Relation",source).items():
        print("  関係者：",target)

#[5] 登場人物を特定して関係者取得
print("\n******************************")
print("Leviに関連する人物を探します")
print("******************************")
#ラベル用辞書の初期化
labellist={}
#関係者を取得
getRelation("Levi",G,1)

# 環境変数からフォントを取得
samplefont=os.environ.get('SAMPLEFONT')
if host ==None:
    host = "TakaoPGothic"

# IPAexフォントを使う場合（事前にインストールが必要）
#nx.draw(G, labels=labellist,font_family='IPAexGothic',font_size=10,
nx.draw(G, labels=labellist,font_family=samplefont,font_size=10,
            node_color="lightblue",edge_color="lightblue",node_size=2000)

plt.savefig("sample1.jpg")
print("\nnetworkxの表示を sample1.jpg　に出力しました")
#接続終了
connection.close()